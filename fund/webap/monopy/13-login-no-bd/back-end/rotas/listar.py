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
    exemplos de testes:

curl -X POST -d '{"login":"josilva@gmail.com"}' localhost:5000/listar/Pessoa
{
  "detalhes": "aus\u00eancia de login josilva@gmail.com na sess\u00e3o", 
  "resultado": "erro"
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
