from src.models import db
from src.models.fazenda import Fazenda

class Produtor(db.Model):
    __tablename__ = 'produtores'

    id = db.Column(db.Integer, primary_key=True)
    cpf_cnpj = db.Column(db.String(18), unique=True, nullable=False)
    nome_produtor = db.Column(db.String(100), nullable=False)

    fazendas = db.relationship('Fazenda', back_populates='produtor', cascade="all, delete-orphan")  # Relacionamento 1:N

    def to_dict(self):
        return {
            'id': self.id,
            'cpf_cnpj': self.cpf_cnpj,
            'nome_produtor': self.nome_produtor,
            'fazendas': [fazenda.to_dict() for fazenda in self.fazendas]  # Inclui as fazendas do produtor
        }
