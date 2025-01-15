
from src.models import db
from sqlalchemy.dialects.postgresql import ARRAY


class Fazenda(db.Model):
    __tablename__ = 'fazendas'

    id = db.Column(db.Integer, primary_key=True)
    nome_fazenda = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    area_total = db.Column(db.Float, nullable=False)
    area_agricultavel = db.Column(db.Float, nullable=False)
    area_vegetacao = db.Column(db.Float, nullable=False)
    culturas = db.Column(ARRAY(db.String), nullable=False)

    produtor_id = db.Column(db.Integer, db.ForeignKey('produtores.id'), nullable=False)  # Referência para Produtor
    produtor = db.relationship('Produtor', back_populates='fazendas')  # Relacionamento inverso


    def to_dict(self):
        return {
            'id': self.id,
            'nome_fazenda': self.nome_fazenda,
            'cidade': self.cidade,
            'estado': self.estado,
            'area_total': self.area_total,
            'area_agricultavel': self.area_agricultavel,
            'area_vegetacao': self.area_vegetacao,
            'culturas': self.culturas,
            'produtor_id': self.produtor_id
        }

        