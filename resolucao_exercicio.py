from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    return 'OK', 200

#Teste resolvido
@app.route('/test1', methods=['GET'])
def test1():
    return jsonify({'message': 'Olá mundo!'}), 200

@app.route('/test2', methods=['POST'])
def test2():
    # Request pode ter: dados de entrada
    data = request.json
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    soma = num1 + num2 
    
    return jsonify({'message': str(soma)}), 200

@app.route('/test3', methods=['POST'])
def test3():
    data = request.json # {}
    numero = data.get('numbers', []) # { 'numbers': [1,2,3,5,6] }
    return jsonify({'message': str(sorted(numero))}),  200
    
@app.route('/test4', methods=['POST'])
def test4():
    data = request.json
    
    return jsonify(
        {
            'nome': data.get('telefone'),
            'telefone': data.get('nome')
        }
    ), 200

@app.route('/test6', methods=['POST'])
def test6():
    id_to_exclude = request.args.get('id', type=int) #Recebe o ID para excluir
    data = request.json #lista de contatos
    
    response = None
    for item in data:
        if item['id'] == id_to_exclude:
            response = item
    
    if response:
        pass
    else:
        response = 'ID não encontrado'
            
    lista_com_id_excluido = []
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
