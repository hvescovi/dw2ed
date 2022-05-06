from configuracoes import *
from modelo import *

if utilizar == "sqlite":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

# criar tabelas
db.create_all()