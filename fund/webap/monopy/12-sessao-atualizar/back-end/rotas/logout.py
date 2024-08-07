from geral import *
from modelo.Pessoa import *

@app.route("/logout", methods=['POST'])
def login():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json()  
    # remover o usuário da sessão
    session.pop(dados['login'], default=None) # caso não exista, seta para None
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    return resposta  # responder!

''' 
RESULTADOS DE TESTES:

curl -X POST -d '{"login":"mylogin"}' -H "Content-Type:application/json" localhost:5000/logout
{
  "detalhes": "ok", 
  "resultado": "ok"
}



'''