# exemplo mínimo
# derivado de: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# configurações
app = Flask(__name__) # vínculo com o Flask
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'compania_1000.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app) # vínculo com o SQLAlchemy

# para exibir versões das bibliotecas:
# pip3 freeze
# para instalar requisitos:
# pip3 install -r requirements.txt
# ou:
# pip3 install flask
# pip3 install flask_sqlalchemy