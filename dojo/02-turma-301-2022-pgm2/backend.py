from config import *
from modelo import Carro

@app.route("/")
def inicio():
    return "sistema de cadastro de carro. "

@app.route("/listar_carros")
def listar_carros():
    carros= db.session.query(Carro).all()
    dados = [x.json() for x in carros]
    resposta = jsonify(dados)
    
    resposta.headers.add("Acess-Control-Allow-Origin", "*")
    return resposta

app.run(debug = True)