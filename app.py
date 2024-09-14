from flask import Flask, jsonify
from src.Schemas.Contatos import contato_schema, contatos_schema, contatos_nomes_schema

app = Flask (__name__)

contatos = [
    {
        'nome': 'João',
        'telefone': '986542131',
        'endereco': 'Av. Brasil, 210'
    },
    {
        'nome': 'Maria',
        'telefone': '985184408',
        'endereco': 'Rod. Gov. Valadares, 700'
    },
    {
        'nome': 'Erick',
        'telefone': '918284984',
        'endereco': 'Rod. Gov. Valadares, 700',
        'cpf': '852.258.258-30'
    },
]


def health():
    versao = '0.0.1'
    return versao

def responseConstructor(context : any, message : str):
    return jsonify({
        'data': context,
        'message': message,
        'API Doc': health()
    })

@app.route('/', methods=['GET'])
def index ():
    return responseConstructor({'API Name': 'Gestor de contatos'}, "OK")

@app.route('/contatos', methods=['GET'])
def listar_contatos():
    result = contatos_schema.dump(contatos)
    return responseConstructor(result, 'Operação realizada com sucesso'), 200

if __name__ == '__main__':
    app.run(debug=True)