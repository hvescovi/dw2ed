from geral.config import *
from geral.cripto import *
from modelo.pessoa import *

@app.route("/login", methods=['POST'])
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

$ curl -c /tmp/cookie -X POST -d '{"login":"josilva@gmail.com", "senha":"joao123"}' localhost:5000/login
{
  "detalhes": "ok", 
  "resultado": "ok"
}

curl -b /tmp/cookie -X POST -d '{"login":"josilva@gmail.com"}' localhost:5000/listar/Pessoa
{
  "detalhes": [
    {
      "email": "josilva@gmail.com", 
      "id": 1, 
      "nome": "Jo\u00e3o da Silva", 
      "senha": "53d32ccc72f314a7c2055f76bc938151b3a0b83861c8ec60a05dfd355f456b5c5fafbd0470da1bdefbbf1f9a9b256990e9c69b5faf93f6d79305ea1e4f7db9b5", 
      "telefone": "47 99012 3232"
    }, 
    {
      "email": "molive@gmail.com", 
      "id": 2, 
      "nome": "Maria Oliveira", 
      "senha": "c31bdc2870e80708a57d0f8577f7d8b08ca4361f0a8528baf71cdcb00086e005b3b2d139d3f0d6192e17f354680c5f915c20a8118d90bec16af818e49ae73da2", 
      "telefone": "47 98822 2531"
    }
  ], 
  "resultado": "ok"
}
 
'''