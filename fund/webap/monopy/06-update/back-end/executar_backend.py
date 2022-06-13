from geral.config import *
import import_modelos
from rotas.listar import *
from rotas.retornar import *
from rotas.atualizar import *

@app.route("/")
def inicio():
    return 'backend operante, operação de editar'

app.run(debug=True)