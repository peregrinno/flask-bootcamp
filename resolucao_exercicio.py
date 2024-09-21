from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    return 'OK', 200


if __name__ == '__main__':
    app.run(debug=True)
