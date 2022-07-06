# importações
from flask import Flask, jsonify, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
from datetime import timedelta

from flask_cors import CORS  # permitir back receber json do front

# configurações
app = Flask(__name__)

# endereço DESTE servidor, que deverá ser chamado 
# no navegador pelo front-end
# (endereço do host liberado para as rotas)
#meuservidor = "http://192.168.5.227"
meuservidor = "http://localhost:81"

CORS(app, supports_credentials = True)  

# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'pessoa.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # remover warnings
db = SQLAlchemy(app)

app.secret_key = '$#EWFGHJUI*&DEGBHYJU&Y%T#RYJHG%##RU&U'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2)
Session(app)

# remoção automática dos arquivos
# https://stackoverflow.com/questions/53841909/clean-server-side-session-files-flask-session-using-filesystem