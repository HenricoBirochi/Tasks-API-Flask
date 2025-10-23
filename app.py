from flask import Flask
from extensions import db
from controller.task_controller import task_bp

# Configuração do app Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)

# Registro do Blueprint de tarefas
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)