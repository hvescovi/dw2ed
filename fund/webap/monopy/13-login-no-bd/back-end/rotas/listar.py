from geral.config import *
from modelo.pessoa import *

@app.route("/listar/<string:classe>")
def listar(classe):
    # obter os dados da classe informada
    dados = None
    if classe == "Pessoa":
      dados = db.session.query(Pessoa).all()
    # converter dados para json
    lista_jsons = [ x.json() for x in dados ]
    # converter a lista do python para json
    resposta = jsonify(lista_jsons)
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    # permitir envio do cookie
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    return resposta

# https://stackoverflow.com/questions/2870371/why-is-jquerys-ajax-method-not-sending-my-session-cookie

    '''
    exemplo de teste:
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