from flask import Flask, jsonify, request
from Contatos import contato_schema, contatos_schema
from marshmallow import ValidationError

app = Flask(__name__)

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
]

def health():
    versao = '0.0.1'
    return versao

def responseConstructor(context, message):
    return jsonify({
        'data': context,
        'message': message,
        'API Doc': health()
    })

def contato_existe(nome=None, telefone=None):
    for contato in contatos:
        if nome and contato['nome'] == nome:
            return True
        if telefone and contato['telefone'] == telefone:
            return True
    return False

@app.route('/contatos', methods=['GET'])
def listar_contatos():
    result = contatos_schema.dump(contatos)
    return responseConstructor(result, 'Operação realizada com sucesso.'), 200

@app.route('/contato/<string:nome>', methods=['GET'])
def obter_contato(nome):
    for contato in contatos:
        if contato['nome'] == nome:
            return responseConstructor(contato, 'Contato encontrado com sucesso.'), 200
    return responseConstructor({}, 'Contato não encontrado.'), 404

@app.route('/novo_contato', methods=['POST'])
def novo_contato():
    json_data = request.json
    try:
        data = contato_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Verifica se o contato com o mesmo nome ou telefone já existe
    if contato_existe(nome=data['nome']) or contato_existe(telefone=data['telefone']):
        return responseConstructor({}, 'Contato com o mesmo nome ou telefone já existe.'), 400

    contatos.append(data)
    return responseConstructor(data, 'Contato salvo com sucesso.'), 201

@app.route('/contato/<string:nome>', methods=['PUT'])
def editar_contato(nome):
    json_data = request.json
    try:
        data = contato_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for contato in contatos:
        if contato['nome'] == nome:
            # Verifica se o novo nome ou telefone já existe em outro contato
            if (data['nome'] != nome and contato_existe(nome=data['nome'])) or contato_existe(telefone=data['telefone']):
                return responseConstructor({}, 'Contato com o mesmo nome ou telefone já existe.'), 400

            contato.update(data)
            return responseConstructor(contato, 'Contato atualizado com sucesso.'), 200
    
    return responseConstructor({}, 'Contato não encontrado.'), 404

@app.route('/contato/<string:nome>', methods=['DELETE'])
def deletar_contato(nome):
    global contatos
    for contato in contatos:
        if contato['nome'] == nome:
            contatos = [c for c in contatos if c['nome'] != nome]
            return responseConstructor(contato, 'Contato deletado com sucesso.'), 200
    return responseConstructor({}, 'Contato não encontrado.'), 404

if __name__ == '__main__':
    app.run(debug=True)
