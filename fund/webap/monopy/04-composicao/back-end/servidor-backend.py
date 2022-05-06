from config import *
from modelo import Pessoa, ExameRealizado, Respirador, Exame

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_pessoas">Operação listar</a>'

@app.route("/listar_pessoas")
def listar_pessoas():
    # obter as pessoas do cadastro
    pessoas = db.session.query(Pessoa).all()
    # aplicar o método json que a classe Pessoa possui a cada elemento da lista
    pessoas_em_json = [ x.json() for x in pessoas ]
    # converter a lista do python para json
    resposta = jsonify(pessoas_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

# teste da rota: curl -d '{"nome":"James Kirk", "telefone":"92212-1212", "email":"jakirk@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_pessoa
@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      nova = Pessoa(**dados) # criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

@app.route("/listar_exames_realizados")
# o código da função abaixo é similar ao código da função listar_pessoas
# será que dava pra generalizar essa função? :-)
def listar_exames_realizados():
    # obter exames realizados
    exames_realizados = db.session.query(ExameRealizado).all()
    # converter dados para json
    lista_jsons = [ x.json() for x in exames_realizados ]
    # converter a lista do python para json
    resposta = jsonify(lista_jsons)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
'''
$ curl localhost:5000/listar_exames_realizados
[
  {
    "data": "02/02/2020", 
    "exame": {
      "id": 1, 
      "nome": "B12", 
      "unidade": "pg/mL", 
      "vr": "239 a 931"
    }, 
    "exame_id": 1, 
    "id": 1, 
    "pessoa": {
      "email": "josilva@gmail.com", 
      "id": 1, 
      "nome": "Jo\u00e3o da Silva", 
      "telefone": "47 99012 3232"
    }, 
    "pessoa_id": 1, 
    "resultado": "219,0 pg/mL"
  }
]
'''

# teste da rota: curl -d '{"data": "18/11/2020", "exame_id": 1, "pessoa_id": 1, "resultado": "230,0 pg/mL" }' -X POST -H "Content-Type:application/json" localhost:5000/incluir_exame_realizado
@app.route("/incluir_exame_realizado", methods=['post'])
def incluir_exame_realizado():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações
    dados = request.get_json()
    try: # tentar executar a operação
      nova = ExameRealizado(**dados) # criar o novo exame realizado
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!
    
app.run(debug=True)