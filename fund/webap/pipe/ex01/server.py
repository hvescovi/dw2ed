from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['get'])
def padrao():
    return "ok servidor online"

# rota padrão: recebimento de dados em json
@app.route("/", methods=['post'])
def receber():
    dados = request.get_json()
    resposta = "Dados recebidos, obrigado! ==> " + str(dados)
    return resposta

app.run(debug=True)
