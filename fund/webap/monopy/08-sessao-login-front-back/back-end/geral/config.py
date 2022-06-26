# importações
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
#from flask_session import Session
import os

from flask_cors import CORS # permitir back receber json do front

# configurações
app = Flask(__name__)
CORS(app) # aplicar o cross domain
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'pessoa.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

# https://flask-session.readthedocs.io/en/latest/
# https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/
# https://stackoverflow.com/questions/43499159/flask-runtimeerror-the-session-is-unavailable-because-no-secret-key-was-set-whe
#Session(app)
#app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "redis"
#app.config['SECRET_KEY'] = "123jajaj"
#app.secret_key = "123jajaj"
#sess = Session()
#sess.init_app(app)

# https://testdriven.io/blog/flask-sessions/

app.secret_key = "123deoliveira4"