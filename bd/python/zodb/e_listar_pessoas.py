from ZODB import FileStorage,DB
import transaction
from c_pessoa import Pessoa

storage = FileStorage.FileStorage('dados/meubd.fs')
db=DB(storage)
connection=db.open()
root=connection.root()

# percorrer as pessoas
for pe in root['pessoas']:
    print(pe)

connection.close()