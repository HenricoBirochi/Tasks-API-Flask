from flask import Blueprint, request, jsonify
from extensions import db
from model.task import Task


task_bp = Blueprint('task_bp', __name__, url_prefix='/tasks')


@task_bp.route('', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    if not tasks:
        return jsonify({'error': 'No tasks found'}), 200
    
    tasks_result = []
    for task in tasks:
        tasks_result.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed
        })
    
    return jsonify(tasks_result), 200


@task_bp.route('', methods=['POST'])
def post_task():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid body requisition data'}), 400
    task = Task(title=data['title'], description=data['description'])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created successfully",
                    "task": task.to_dict()}), 201


@task_bp.route('/<int:task_id>', methods=['PUT'])
def put_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid body requisition data'}), 400

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    db.session.commit()

    return jsonify({"message": "Task updated successfully",
                    "task": task.to_dict()}), 200


@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'}), 200
