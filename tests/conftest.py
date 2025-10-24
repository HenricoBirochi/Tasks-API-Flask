from pytest import fixture
from flask import Flask
from sqlalchemy.pool import StaticPool

from extensions import db
from controllers.task_controller import task_bp


@fixture(scope="session")
def app():
    # App isolado para testes, não toca o app de produção
    test_app = Flask(__name__)
    test_app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite://",
        SQLALCHEMY_ENGINE_OPTIONS={
            "connect_args": {"check_same_thread": False},
            "poolclass": StaticPool,
        },
    )

    db.init_app(test_app)
    test_app.register_blueprint(task_bp)

    with test_app.app_context():
        db.drop_all()
        db.create_all()
        yield test_app
        db.session.remove()
        db.drop_all()


@fixture()
def client(app):
    return app.test_client()

