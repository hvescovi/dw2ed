from geral.config import *
from modelo.pessoa import *

@app.route("/listar/<string:classe>", methods=['POST'])
def listar(classe):
    # receber dados da requisição
    dados = request.get_json(force=True)

    # não foi passado login?
    if 'login' not in dados:
        resposta = jsonify({"resultado": "erro", "detalhes": "ausência de login na requisição"})
    else:
        # obtém o login informado
        login = dados['login']
        # o login informado existe na sessão?
        valor = None
        try:
            valor = session[login]
            print("valor na sessão: " + valor)
        except Exception as e:
            print("não encontrado: "+str(e))
        if valor == None:
            resposta = jsonify({"resultado": "erro", "detalhes": "ausência de login "+dados['login']+" na sessão"})
        else:    
            dados = None
            if classe == "Pessoa":
                dados = db.session.query(Pessoa).all()

            # converter dados para json
            lista_jsons = [x.json() for x in dados]
            # converter a lista do python para json
            resposta = jsonify({"resultado":"ok","detalhes":lista_jsons})

    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    # permitir envio do cookie
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    return resposta

    '''
    exemplo de teste:
    $ curl -X POST -d '{"login":"josilva@gmail.com"} localhost:5000/listar/ExameRealizado
'''
