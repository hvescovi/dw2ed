from geral.config import *
from modelo.Pessoa import *

if os.path.exists(arquivobd):
    os.remove(arquivobd)

# criar tabelas
db.create_all()

print("Banco de dados e tabelas criadas")