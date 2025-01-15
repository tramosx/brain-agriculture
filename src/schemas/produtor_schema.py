from marshmallow import Schema, fields, validate

class FazendaSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome_fazenda = fields.Str(required=True)
    cidade = fields.Str(required=True)
    estado = fields.Str(required=True, validate=validate.Length(equal=2))
    area_total = fields.Float(required=True)
    area_agricultavel = fields.Float(required=True)
    area_vegetacao = fields.Float(required=True)
    culturas = fields.List(fields.String, required=True)

class ProdutorSchema(Schema):
    cpf_cnpj = fields.Str(required=True)
    nome_produtor = fields.Str(required=True)
    fazendas = fields.List(fields.Nested(FazendaSchema), required=True)
