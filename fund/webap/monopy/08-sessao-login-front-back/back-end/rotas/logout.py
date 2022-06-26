from geral.config import *
from modelo.Pessoa import *

@app.route("/logout", methods=['POST'])
def login():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json()  
    login = dados['login']
    if session.get(login) == True:
        # armazenar sessão, para informar que há login realizado
        session.pop(login)
    else:
        resposta = jsonify({"resultado": "erro", "detalhes": "login não encontrado na sessão"})        
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!

''' 
RESULTADOS DE TESTES:

curl -X POST -d '{"login":"mylogin"}' -H "Content-Type:application/json" localhost:5000/logout
{
  "detalhes": "ok", 
  "resultado": "ok"
}


curl -X GET -d '{"login":"mylogin", "senha":"1234"}' -H "Content-Type:application/json" localhost:5000/login
{
  "detalhes": "login e/ou senha inv\u00e1lido(s)", 
  "resultado": "erro"
}


'''