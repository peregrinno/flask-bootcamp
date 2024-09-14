from marshmallow import Schema, fields

class ContatoSchema(Schema):
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    endereco = fields.Str(required=True)

contato_schema = ContatoSchema()
contatos_schema = ContatoSchema(many=True)