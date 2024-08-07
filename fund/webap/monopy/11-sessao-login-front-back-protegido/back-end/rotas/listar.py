from geral import *
from modelo.Pessoa import *

@app.route("/listar/<string:classe>", methods=['POST'])
def listar(classe):
    dados = request.get_json(force=True)  
    try:  
        # obtem login da sessao
        login = session[dados['login']]
        # obter os dados da classe informada
        if classe == "Pessoa":
            dados = db.session.query(Pessoa).all()
        # converter dados para json
        lista_jsons = [ x.json() for x in dados ]
        # converter a lista do python para json
        resposta = jsonify(lista_jsons)
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        print("ERRO: "+str(e))
      
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    # permitir o envio dos cookies
    resposta.headers.add('Access-Control-Allow-Credentials', 'true')
    return resposta

# https://github.com/corydolphin/flask-cors/issues/200
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