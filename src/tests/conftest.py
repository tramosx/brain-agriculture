import pytest
from app import create_app
from src.models import db


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def novo_produtor():
    return {
        "nome_produtor": "teste",
        "nome_fazenda": "fazenda teste",
        "cpf_cnpj": "05427781064",
        "email": "joao.silva@example.com",
        "area_total": 100,
        "area_agricultavel": 60,
        "area_vegetacao": 40,
        "estado": "ba",
        "cidade": "salvador",
        "culturas": [
            "Soja"
        ],
    }