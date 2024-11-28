from src.models import db


class Produtor(db.Model):
    __tablename__ = 'produtores'

    id = db.Column(db.Integer, primary_key=True)
    cpf_cnpj = db.Column(db.String(18), unique=True, nullable=False)
    nome_produtor = db.Column(db.String(100), nullable=False)
    nome_fazenda = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    area_total = db.Column(db.Float, nullable=False)
    area_agricultavel = db.Column(db.Float, nullable=False)
    area_vegetacao = db.Column(db.Float, nullable=False)
    culturas = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cpf_cnpj': self.cpf_cnpj,
            'nome_produtor': self.nome_produtor,
            'nome_fazenda': self.nome_fazenda,
            'cidade': self.cidade,
            'estado': self.estado,
            'area_total': self.area_total,
            'area_agricultavel': self.area_agricultavel,
            'area_vegetacao': self.area_vegetacao,
            'culturas': self.culturas.split(',') if self.culturas else []
        }
