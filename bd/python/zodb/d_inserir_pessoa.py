from ZODB import FileStorage,DB
import transaction
from c_pessoa import Pessoa

storage = FileStorage.FileStorage('dados/meubd.fs')
db=DB(storage)
connection=db.open()
root=connection.root()

p = Pessoa()
p.nome = "João da Silva"
p.email = "josilva@mail.com"
p.peso = 70

pessoas = [p]
root['pessoas'] = pessoas

transaction.commit()

print(root.items)

# percorrer as pessoas
for pe in root['pessoas']:
    print(pe)

connection.close()