# importações
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask.ext.session import Session
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
Session(app)