from geral.config import *
import import_modelos
from rotas.listar import *
from rotas.incluir import *

@app.route("/")
def inicio():
    return 'backend com rotas generalizadas de listagem'

app.run(debug=True)