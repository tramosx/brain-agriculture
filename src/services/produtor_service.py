from src.models.produtor import db, Produtor, Fazenda
from src.utils.validacoes import valida_cpf_cnpj, valida_areas
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func


class ProdutorService:
    @staticmethod
    def cadastrar_produtor(data):
        if not valida_cpf_cnpj(data['cpf_cnpj']):
            raise ValueError('CPF/CNPJ inválido')

        produtor = Produtor(
            cpf_cnpj=data['cpf_cnpj'],
            nome_produtor=data['nome_produtor']
        )

        for fazenda_data in data['fazendas']:
            if not valida_areas(fazenda_data['area_total'], fazenda_data['area_agricultavel'], fazenda_data['area_vegetacao']):
                raise ValueError('Áreas inválidas')

            fazenda = Fazenda(
                nome_fazenda=fazenda_data['nome_fazenda'],
                cidade=fazenda_data['cidade'],
                estado=fazenda_data['estado'],
                area_total=fazenda_data['area_total'],
                area_agricultavel=fazenda_data['area_agricultavel'],
                area_vegetacao=fazenda_data['area_vegetacao'],
                culturas=fazenda_data['culturas']
            )

            fazenda.produtor = produtor

            db.session.add(fazenda)

        db.session.add(produtor)

        db.session.commit()

        return produtor

    def editar_fazenda(produtor_id, fazenda_id, data):
        produtor = Produtor.query.get(produtor_id)

        if not produtor:
            raise ValueError("Produtor não encontrado.")


        fazenda = Fazenda.query.filter_by(id=fazenda_id, produtor_id=produtor.id).first()
        if not fazenda:
            raise ValueError(f"Fazenda com id {fazenda_id} não encontrada para o produtor com id {produtor_id}.")

        fazenda.nome_fazenda = data.get('nome_fazenda', fazenda.nome_fazenda)
        fazenda.cidade = data.get('cidade', fazenda.cidade)
        fazenda.estado = data.get('estado', fazenda.estado)
        fazenda.area_total = data.get('area_total', fazenda.area_total)
        fazenda.area_agricultavel = data.get('area_agricultavel', fazenda.area_agricultavel)
        fazenda.area_vegetacao = data.get('area_vegetacao', fazenda.area_vegetacao)
        fazenda.culturas = data.get('culturas', fazenda.culturas)

        db.session.commit()

        return fazenda


    @staticmethod
    def excluir_produtor(id):
        produtor = Produtor.query.get(id)
        
        if not produtor:
            raise ValueError("Produtor não encontrado.")
        
        db.session.delete(produtor)
        db.session.commit()

    @staticmethod
    def listar_produtores():
        return Produtor.query.all()

    @staticmethod
    def contar_fazendas():
        return Fazenda.query.count()  # Retorna o número total de fazendas

    @staticmethod
    def somar_area():
        """Retorna a soma da área total (em hectares) de todas as fazendas"""
        total_area_hectares = Fazenda.query.with_entities(Fazenda.area_total).all()
        return sum(fazenda[0] for fazenda in total_area_hectares)  # Soma de todas as áreas


    @staticmethod
    def grafico_pizza_por_estado():
        """Retorna a contagem de fazendas agrupadas por estado"""
        estados = Fazenda.query.with_entities(Fazenda.estado, func.count(Fazenda.id).label('quantidade')) \
                               .group_by(Fazenda.estado).all()
        return {estado: quantidade for estado, quantidade in estados}


    @staticmethod
    def grafico_pizza_por_cultura():
        """Retorna a contagem de fazendas agrupadas por cultura"""
        culturas = Fazenda.query.with_entities(Fazenda.culturas)  # Supondo que 'culturas' seja uma lista de strings
        cultura_count = {}
        
        for cultura in culturas:
            for c in cultura[0]:  # Aqui, cultura[0] é a lista de culturas
                if c in cultura_count:
                    cultura_count[c] += 1
                else:
                    cultura_count[c] = 1
        
        return cultura_count


    @staticmethod
    def grafico_pizza_por_uso_solo():
        """Retorna a soma das áreas agricultáveis e de vegetação"""
        areas = Fazenda.query.with_entities(Fazenda.area_agricultavel, Fazenda.area_vegetacao).all()
        area_agricultavel_total = sum(area[0] for area in areas)
        area_vegetacao_total = sum(area[1] for area in areas)
        
        
        return {
            "Agricultável": area_agricultavel_total,
            "Vegetação": area_vegetacao_total
        }