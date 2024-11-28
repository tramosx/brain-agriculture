from flask import Blueprint, request, jsonify
from src.services.produtor_service import ProdutorService
from src.utils.validacoes import valida_cpf_cnpj, valida_areas

from sqlalchemy.exc import IntegrityError


routes_blueprint = Blueprint('produtores', __name__)

@routes_blueprint.route('/produtores', methods=['POST'])
def cadastrar_produtor():
    data = request.get_json()
    if not valida_cpf_cnpj(data['cpf_cnpj']):
        return jsonify({'error': 'CPF/CNPJ inválido'}), 400
    if not valida_areas(data['area_total'], data['area_agricultavel'], data['area_vegetacao']):
        return jsonify({'error': 'Áreas inválidas'}), 400

    try:
        produtor = ProdutorService.cadastrar_produtor(data)
        return jsonify(produtor.to_dict()), 201
    except IntegrityError as e:
        ProdutorService.rollback()
        if 'duplicate key value violates unique constraint' in str(e.orig):
            return jsonify({
                'error': 'Chave duplicada',
                'message': f"O CPF/CNPJ '{data.get('cpf_cnpj')}' já está cadastrado."
            }), 400
        return jsonify({'error': 'Erro de banco de dados', 'message': str(e)}), 500
    
    except Exception as e:
        return jsonify({'error': 'Erro inesperado', 'message': str(e)}), 500


@routes_blueprint.route('/produtores/<int:id>', methods=['PUT'])
def editar_produtor(id):
    data = request.get_json()
    produtor = ProdutorService.editar_produtor(id, data)
    return jsonify(produtor.to_dict()), 200

@routes_blueprint.route('/produtores/<int:id>', methods=['DELETE'])
def excluir_produtor(id):
    ProdutorService.excluir_produtor(id)
    return jsonify({'message': 'Produtor excluído com sucesso'}), 200

@routes_blueprint.route('/produtores', methods=['GET'])
def listar_produtores():
    produtores = ProdutorService.listar_produtores()
    return jsonify([produtor.to_dict() for produtor in produtores]), 200
