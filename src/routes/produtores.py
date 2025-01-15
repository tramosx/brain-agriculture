from flask import Blueprint, request, jsonify
from src.services.produtor_service import ProdutorService
from src.utils.validacoes import valida_cpf_cnpj, valida_areas
from sqlalchemy.exc import IntegrityError
from src.schemas.produtor_schema import ProdutorSchema, FazendaSchema
from src.models import db


routes_blueprint = Blueprint('produtores', __name__)

@routes_blueprint.route('/produtores', methods=['POST'])
def cadastrar_produtor():
    data = request.get_json()
    schema = ProdutorSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    try:
        produtor = ProdutorService.cadastrar_produtor(data)
        return jsonify(produtor.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Produtor já Cadastrado!'}), 500


@routes_blueprint.route('/produtores/<int:produtor_id>/fazendas/<int:fazenda_id>', methods=['PUT'])
def editar_fazenda(produtor_id, fazenda_id):
    data = request.get_json()

    schema = FazendaSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    try:
        fazenda = ProdutorService.editar_fazenda(produtor_id, fazenda_id, data)
        return jsonify(fazenda.to_dict()), 200  # Retorna os dados da fazenda atualizada
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@routes_blueprint.route('/produtores/<int:id>', methods=['DELETE'])
def excluir_produtor(id):
    try:
        ProdutorService.excluir_produtor(id)
        return jsonify({'message': 'Produtor excluído com sucesso'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Erro inesperado', 'message': str(e)}), 500


@routes_blueprint.route('/produtores', methods=['GET'])
def listar_produtores():
    produtores = ProdutorService.listar_produtores()
    return jsonify([produtor.to_dict() for produtor in produtores]), 200


@routes_blueprint.route('/fazendas/total', methods=['GET'])
def total_fazendas():
    total_fazendas = ProdutorService.contar_fazendas()  # Usando o serviço

    total_area = ProdutorService.somar_area()

    grafico_estado = ProdutorService.grafico_pizza_por_estado()
    
    grafico_cultura = ProdutorService.grafico_pizza_por_cultura()
    
    grafico_uso_solo = ProdutorService.grafico_pizza_por_uso_solo()

    return jsonify({
        "total_fazendas": total_fazendas,
        "total_area_hectares": total_area,
        "grafico_estado": grafico_estado,
        "grafico_cultura": grafico_cultura,
        "grafico_uso_solo": grafico_uso_solo
    }), 200


    return jsonify({"total_fazendas": total_fazendas}), 200


