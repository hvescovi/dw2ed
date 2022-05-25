from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['get'])
def padrao():
    return "ok servidor online"

# rota padrão: recebimento de dados em json
@app.route("/", methods=['post'])
def receber():
    dados = request.json
    return dados

app.run(debug=True)