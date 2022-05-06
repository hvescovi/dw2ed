from config import *
from modelo import Pessoa, ExameRealizado, Respirador, Exame

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_pessoas">Operação listar</a>'




# teste: curl -X DELETE http://localhost:5000/excluir_pessoa/1
@app.route("/excluir_pessoa/<int:pessoa_id>", methods=['DELETE'])
def excluir_pessoa(pessoa_id):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        # excluir a pessoa do ID informado
        Pessoa.query.filter(Pessoa.id == pessoa_id).delete()
        # confirmar a exclusão
        db.session.commit()
    except Exception as e:
        # informar mensagem de erro
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

''' teste da exclusão:
$ curl -X DELETE http://localhost:5000/excluir_pessoa/1
{
  "detalhes": "ok", 
  "resultado": "ok"
}
'''

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

@app.route("/listar/<string:classe>")
# mais uma função similar à listar_pessoa :-/ vamos tentar generalizar :-)
def listar(classe):
    # obter os dados da classe informada
    dados = None
    if classe == "ExameRealizado":
      dados = db.session.query(ExameRealizado).all()
    elif classe == "Pessoa":
      dados = db.session.query(Pessoa).all()
    elif classe == "Respirador":
      dados = db.session.query(Respirador).all()
    elif classe == "Exame":
      dados = db.session.query(Exame).all()
    # converter dados para json
    lista_jsons = [ x.json() for x in dados ]
    # converter a lista do python para json
    resposta = jsonify(lista_jsons)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
    '''
    $ curl localhost:5000/listar/ExameRealizado
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

app.run(debug=True)