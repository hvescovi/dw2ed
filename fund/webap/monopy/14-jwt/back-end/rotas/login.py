from geral.config import *
from geral.cripto import *
from modelo.pessoa import *

@app.route("/login", methods=['POST'])
def login():

    dados = request.get_json(force=True)  
    login = dados['login']
    senha = dados['senha']
    
    encontrado = Pessoa.query.filter_by(email=login, senha=cifrar(senha)).first()
    if encontrado is None: 
        resposta = jsonify({"resultado": "erro", "detalhes":"usuario ou senha incorreto(s)"})

    else:
        # códigos HTTP:
        # https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status        

        # criar a json web token (JWT)
        access_token = create_access_token(identity=login)

        # retornar
        resposta =  jsonify({"resultado":"ok", "detalhes":access_token}) 
    
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*") #meuservidor)
    # permitir envio do cookie
    #resposta.headers.add("Access-Control-Allow-Credentials", "true")

    return resposta 

''' 
RESULTADOS DE TESTES:

$ curl -X POST localhost:5000/login -d '{"login":"josilva@gmail.com","senha":"joao123"}' -H 'Content-Type: application/json'
{
  "detalhes": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODMxNTEzOSwianRpIjoiZTVmMGVjMGEtOGZjMC00N2QyLWE4YjItOTMzNTY4MjMwZTM5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Impvc2lsdmFAZ21haWwuY29tIiwibmJmIjoxNjU4MzE1MTM5LCJleHAiOjE2NTgzMTYwMzl9.DjTA7h8idYfFpXixYl7gCGtu9rmahlj2IXTtlbkE0nc", 
  "resultado": "ok"
}

$ curl localhost:5000/listar/Pessoa 
{
  "msg": "Missing Authorization Header"
}

$ curl localhost:5000/listar/Pessoa -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODMxNTEzOSwianRpIjoiZTVmMGVjMGEtOGZjMC00N2QyLWE4YjItOTMzNTY4MjMwZTM5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Impvc2lsdmFAZ21haWwuY29tIiwibmJmIjoxNjU4MzE1MTM5LCJleHAiOjE2NTgzMTYwMzl9.DjTA7h8idYfFpXixYl7gCGtu9rmahlj2IXTtlbkE0nc'
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

$ curl -X POST localhost:5000/login -d '{"login":"josilva@gmail.com","senha":"joao1234"}' -H 'Content-Type: application/json'
{
  "detalhes": "usuario ou senha incorreto(s)", 
  "resultado": "erro"
}

 
'''