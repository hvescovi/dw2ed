from geral.config import *

import import_modelos

if os.path.exists(arquivobd):
    os.remove(arquivobd)

# criar tabelas
db.create_all()

print("Banco de dados e tabelas criadas")