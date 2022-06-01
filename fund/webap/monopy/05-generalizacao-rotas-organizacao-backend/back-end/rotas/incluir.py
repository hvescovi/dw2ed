from geral.config import *
from modelo.Pessoa import *
from modelo.Exame import *
from modelo.ExameRealizado import *
from modelo.Respirador import *

# exemplo de teste:
# curl -d '{"nome":"Teresa Có", "email":"teco@gmail.com","telefone":"47 9923-1232"}' -X POST -H 'Content-Type:application/json' localhost:5000/incluir/Pessoa

@app.route("/incluir/<string:classe>", methods=['post'])
def incluir(classe):
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json()  
    try:  
        nova = None
        if classe == "ExameRealizado":
            nova = ExameRealizado(**dados)
        elif classe == "Pessoa":
            nova = Pessoa(**dados)
        elif classe == "Respirador":
            nova = Respirador(**dados)
        elif classe == "Exame":
            nova = Exame(**dados)
        db.session.add(nova)  # adicionar no BD
        db.session.commit()  # efetivar a operação de gravação
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!