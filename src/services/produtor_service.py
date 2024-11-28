from src.models.produtor import db, Produtor

class ProdutorService:
    @staticmethod
    def cadastrar_produtor(data):
        produtor = Produtor(
            cpf_cnpj=data['cpf_cnpj'],
            nome_produtor=data['nome_produtor'],
            nome_fazenda=data['nome_fazenda'],
            cidade=data['cidade'],
            estado=data['estado'],
            area_total=data['area_total'],
            area_agricultavel=data['area_agricultavel'],
            area_vegetacao=data['area_vegetacao'],
            culturas=','.join(data.get('culturas', []))
        )
        db.session.add(produtor)
        db.session.commit()
        return produtor

    @staticmethod
    def editar_produtor(id, data):
        produtor = Produtor.query.get_or_404(id)
        for key, value in data.items():
            if hasattr(produtor, key):
                setattr(produtor, key, value)
        db.session.commit()
        return produtor

    @staticmethod
    def excluir_produtor(id):
        produtor = Produtor.query.get_or_404(id)
        db.session.delete(produtor)
        db.session.commit()

    @staticmethod
    def listar_produtores():
        return Produtor.query.all()


    @staticmethod
    def rollback():
        """
        Reverte a transação atual do banco de dados.
        """
        db.session.rollback()