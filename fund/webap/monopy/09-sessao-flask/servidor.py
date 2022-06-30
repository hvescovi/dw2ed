# https://testdriven.io/blog/flask-server-side-sessions/
# https://stackoverflow.com/questions/15995919/how-to-use-curl-to-send-cookies/23039038#23039038
# https://flask.palletsprojects.com/en/2.0.x/config/#SECRET_KEY

from flask import Flask, request, session, jsonify
from flask_session import Session

app = Flask(__name__)

# a chave secreta é usada para assinar com criptografia os cookies
# usados para armazenar o identificador da sessão
app.secret_key = '$#EWFGHJUI*&DEGBHYJU&Y%T#RYJHG%##RU&U'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def padrao():
    return 'backend server-side.'
    
@app.route('/set', methods=['POST'])
def set():
     # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações
    dados = request.get_json()  
    try:  
        if 'chave' not in dados: # não tem o atributo chave?
            resposta = jsonify({"resultado": "erro", 
                            "detalhes": "Atributo chave não encontrado"})
        else:
            # armazena na sessão :-)
            session[dados['chave']] = dados['valor']
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!

@app.route('/get')
def get():
    try:
        dados = request.get_json()  
        retorno = {'resultado': 'ok'}
        retorno.update({'detalhes': session[dados['chave']]}) # concatenar dois json's (dicionários)
        resposta = jsonify(retorno)
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!

@app.route('/delete')
def delete():
    try:
        dados = request.get_json()  
        session.pop(dados['chave'], default=None)
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})        
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
            
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!

app.run(debug=True)

# teste via curl:
# curl -c /tmp/cookie -X POST -d '{"chave":"email","valor":"hvescovi@hotmail.com"}' -H "Content-Type:application/json" localhost:5000/set
# curl -b "/tmp/cookie" -d '{"chave":"email"}' -X GET -H "Content-Type:application/json"  localhost:5000/get
# curl -b "/tmp/cookie" -d '{"chave":"email"}' -X GET -H "Content-Type:application/json" localhost:5000/delete
