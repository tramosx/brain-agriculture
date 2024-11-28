import pytest
from src.models.produtor import db, Produtor


def test_cadastrar_produtor(client, novo_produtor):
    """Testa a rota de cadastro de produtor."""
    response = client.post('/produtores', json=novo_produtor) 
    assert response.status_code == 201
    assert response.json['cpf_cnpj'] == novo_produtor['cpf_cnpj']


def test_cadastrar_produtor_duplicado(client, novo_produtor):
    """Testa a tentativa de cadastro com CPF/CNPJ duplicado."""
    # Primeiro cadastro
    client.post('/produtores', json=novo_produtor)
    # Cadastro duplicado
    response = client.post('/produtores', json=novo_produtor)
    assert response.status_code == 400
    assert response.json['error'] == "Chave duplicada"


def test_cadastrar_produtor_cpf_invalido(client, novo_produtor):
    """Testa a validação de CPF inválido."""
    novo_produtor['cpf_cnpj'] = '123456789'  # CPF inválido
    response = client.post('/produtores', json=novo_produtor)
    assert response.status_code == 400
    assert response.json['error'] == "CPF/CNPJ inválido"


def test_editar_produtor(client, novo_produtor):
    """Testa a edição de um produtor existente."""
    # Cadastrar produtor
    response = client.post('/produtores', json=novo_produtor)
    produtor_id = response.json['id']

    update_data = {"nome": "João Santos"}
    response = client.put(f'/produtores/{produtor_id}', json=update_data)
    assert response.status_code == 200
    assert response.json['nome_produtor'] == "teste"
