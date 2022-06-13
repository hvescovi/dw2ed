from geral.config import *
from modelo.Pessoa import *

@app.route("/retornar/<string:classe>/<int:id>", methods=['get'])
def retornar(classe, id):
    try:  
        if classe == "Pessoa":
            alguem = Pessoa.query.get(id)
            if alguem is None: # se não encontrou
                resposta = jsonify({"resultado": "erro", 
                            "detalhes": f"Objeto não encontrado, id: {id}"})
            else:
                alguem_j = alguem.json() # obtém a versão json 
                retorno = {'resultado': 'ok'}
                retorno.update({'detalhes': alguem_j}) # concatenar dois json's (dicionários)
                resposta = jsonify(retorno)
        else:
            resposta = jsonify({"resultado": "erro", "detalhes": f"Classe não encontrada: {classe}"})
        
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!

'''
RESULTADOS DE TESTES:

$ curl localhost:5000/retornar/Pessoa/2
{
  "detalhes": {
    "email": "molive@gmail.com", 
    "id": 2, 
    "nome": "Maria Oliveira", 
    "telefone": "47 98822 2531"
  }, 
  "resultado": "ok"
}

$ curl localhost:5000/retornar/Pessoa/3
{
  "detalhes": "Objeto n\u00e3o encontrado, id: 3", 
  "resultado": "erro"
}

$ curl localhost:5000/retornar/Eita/1
{
  "detalhes": "Classe n\u00e3o encontrada: Eita", 
  "resultado": "erro"
}

'''