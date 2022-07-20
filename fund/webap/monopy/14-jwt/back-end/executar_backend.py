from geral.config import *
from modelo import *
from rotas import *

@app.route("/")
def inicio():
    return 'backend operante, operação de editar'

app.run(debug=True) #, host="0.0.0.0")