from geral import *
from modelo.Pessoa import *

# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

@app.route("/atualizar/<string:classe>", methods=['PUT'])
def atualizar(classe):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json()  
    # não foi passado login?
    if 'login' not in dados:
      resposta = jsonify({"resultado": "erro", "detalhes": "ausência de login na requisição"})
    else:
      login = dados['login']
      # o login informado não existe na sessão?
      valor = None
      try:
          valor = session[login]
          print("====> ")
          print(valor)
      except Exception as e:
          print(str(e))
      if valor == None:
          resposta = jsonify({"resultado": "erro", "detalhes": "ausência de login "+dados['login']+" na sessão"})
      else:
        try:  
            if classe == "Pessoa":
                if 'id' not in dados: # não tem o atributo id?
                    resposta = jsonify({"resultado": "erro", 
                                "detalhes": "Atributo id não encontrado"})
                else:
                    id = dados['id']
                    alguem = Pessoa.query.get(id) # localizar a pessoa
                    if alguem is None: # se não encontrou
                        resposta = jsonify({"resultado": "erro", 
                                    "detalhes": f"Objeto não encontrado, id: {id}"})
                    else:
                        # atualizar os campos (esta parte dá pra melhorar :-)
                        alguem.nome = dados['nome'] # if dados['nome'] is not None else alguem.nome
                        alguem.email = dados['email']
                        alguem.telefone = dados['telefone']
                        db.session.commit()  # efetivar a atualização
            else:
                resposta = jsonify({"resultado": "erro", "detalhes": f"Classe não encontrada: {classe}"})        
            
        except Exception as e:  # em caso de erro...
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    #resposta.headers['Access-Control-Allow-Credentials'] = 'true'
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    resposta.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    resposta.headers.add('Access-Control-Allow-Methods', 'POST,PUT,OPTIONS')
    # permitir envio das credenciais
    
    return resposta  # responder!

''' 
RESULTADOS DE TESTES:

$ curl -b "/tmp/cookie" -X PUT -d '{"id":1, "nome":"Tiago", "email":"ti@gmail.com","telefone":"123123123","login":"mylogin"}' -H "Content-Type:application/json" localhost:5000/atualizar/Pessoa
{
  "detalhes": "ok", 
  "resultado": "ok"
}

$ curl localhost:5000/retornar/Pessoa/1
{
  "detalhes": {
    "email": "ti@gmail.com", 
    "id": 1, 
    "nome": "Tiago", 
    "telefone": "123123123"
  }, 
  "resultado": "ok"
}

'''