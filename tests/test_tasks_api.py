import json


def test_get_tasks_empty_returns_message(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    body = resp.get_json()
    # Quando vazio, retorna mensagem
    assert body == {"message": "No tasks found"}


def test_create_task_and_list(client):
    payload = {"title": "Teste 1", "description": "Desc 1"}
    resp = client.post("/tasks", data=json.dumps(payload), content_type="application/json")
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["message"] == "Task created successfully"
    assert body["task"]["id"] > 0
    assert body["task"]["title"] == "Teste 1"
    assert body["task"]["description"] == "Desc 1"
    assert body["task"]["completed"] is False

    # Agora deve listar 1 tarefa
    list_resp = client.get("/tasks")
    assert list_resp.status_code == 200
    list_body = list_resp.get_json()
    assert list_body["total_tasks"] == 1
    assert list_body["tasks"][0]["title"] == "Teste 1"


def test_get_task_not_found(client):
    resp = client.get("/tasks/9999")
    assert resp.status_code == 404
    assert resp.get_json() == {"errors": "Task not found"}


def test_update_task(client):
    # cria
    payload = {"title": "Inicial", "description": "D"}
    resp = client.post("/tasks", data=json.dumps(payload), content_type="application/json")
    task_id = resp.get_json()["task"]["id"]

    # atualiza
    upd = {"title": "Atualizado", "completed": True}
    put_resp = client.put(f"/tasks/{task_id}", data=json.dumps(upd), content_type="application/json")
    assert put_resp.status_code == 200
    put_body = put_resp.get_json()
    assert put_body["message"] == "Task updated successfully"
    assert put_body["task"]["title"] == "Atualizado"
    assert put_body["task"]["completed"] is True

    # confere via GET
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 200
    get_body = get_resp.get_json()
    assert get_body["title"] == "Atualizado"
    assert get_body["completed"] is True


def test_delete_task(client):
    # cria
    payload = {"title": "Apagar", "description": "X"}
    resp = client.post("/tasks", data=json.dumps(payload), content_type="application/json")
    task_id = resp.get_json()["task"]["id"]

    # deleta
    del_resp = client.delete(f"/tasks/{task_id}")
    assert del_resp.status_code == 200
    assert del_resp.get_json() == {"message": "Task deleted"}

    # confirma 404
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
    assert get_resp.get_json() == {"errors": "Task not found"}

