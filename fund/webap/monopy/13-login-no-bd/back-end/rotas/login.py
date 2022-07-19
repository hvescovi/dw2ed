from geral.config import *
from geral.cripto import *
from modelo.pessoa import *

@app.route("/login", methods=['GET'])
def login():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json(force=True)  
    login = dados['login']
    senha = dados['senha']

    # verificar se login e senha estão corretos
    encontrado = Pessoa.query.filter_by(email=login, senha=cifrar(senha)).first()
    if encontrado is not None:
        session[login] = "OK"
    else:
        resposta = jsonify({"resultado": "erro", "detalhes": "login e/ou senha inválido(s)"})        
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    # permitir envio do cookie
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    return resposta  # responder!

''' 
RESULTADOS DE TESTES:

$ curl -c /tmp/cookie -X GET -d '{"login":"josilva@gmail.com", "senha":"joao123"}' localhost:5000/login
{
  "detalhes": "ok", 
  "resultado": "ok"
}


'''