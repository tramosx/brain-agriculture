from flask import Flask
from flask_migrate import Migrate
from config import Config
from src.models import db
from src.routes.produtores import routes_blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar banco de dados
    db.init_app(app)


    migrate = Migrate(app, db)


    # Registrar blueprints
    app.register_blueprint(routes_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
