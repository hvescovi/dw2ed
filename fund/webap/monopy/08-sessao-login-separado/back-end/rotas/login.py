from geral import *
from modelo.Pessoa import *

@app.route("/login", methods=['POST'])
def login():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json()  
    login = dados['login']
    senha = dados['senha']
    if login == 'mylogin' and senha == '123':
        pass
    else:
        resposta = jsonify({"resultado": "erro", "detalhes": "login e/ou senha inválido(s)"})        
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!

''' 
RESULTADOS DE TESTES:

curl -X POST -d '{"login":"mylogin", "senha":"123"}' -H "Content-Type:application/json" localhost:5000/login
{
  "detalhes": "ok", 
  "resultado": "ok"
}


curl -X POST -d '{"login":"mylogin", "senha":"1234"}' -H "Content-Type:application/json" localhost:5000/login
{
  "detalhes": "login e/ou senha inv\u00e1lido(s)", 
  "resultado": "erro"
}


'''