from config import *
from modelo import Pessoa
from datetime import date

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/incluir">Operação incluir pessoa</a>'

# teste da rota:
#curl -d '{"nome":"João da Silva", "mensagem":"Viva o momento e faça planos", "dtnasc":"1976-10-28", "peso":"73.5"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_pessoa

@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "oi"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição

    # tratamento especial para data
    partes = dados['dtnasc'].split("-")
    # substituir o item original do dicionário por um valor do python
    dados['dtnasc'] = date(int(partes[0]), int(partes[1]), int(partes[2]))

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

app.run()#debug=True)