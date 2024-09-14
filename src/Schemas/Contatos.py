from marshmallow import Schema, fields

class ContatoSchema(Schema):
    nome = fields.Str(required=True)
    telefone = fields.Str(required=True)
    endereco = fields.Str(required=True)
    cpf = fields.Str(required=False)

class ContatoNomeSchema(Schema):
    nome = fields.Str(required=True)
    
contato_schema = ContatoSchema() #Esse objeto aceita um contato
contatos_schema = ContatoSchema(many=True) #Esse objeto aceita muito contatos

contatos_nomes_schema = ContatoNomeSchema(many=True)