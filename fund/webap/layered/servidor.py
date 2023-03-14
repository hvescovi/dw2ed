# importações
from flask import Flask, render_template
import os
from modelo import Pessoa
import DAO as dao

# configurações
app = Flask(__name__)

# rotas

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_pessoas">Operação listar</a>'

@app.route("/listar_pessoas")
def listar_pessoas():
    # obter as pessoas do cadastro
    pessoas = dao.retornarPessoas()
    # fornecer a lista de pessoas para a página que exibe as pessoas
    return render_template("listar-pessoas.html", listagem = pessoas)

app.run(debug=True)