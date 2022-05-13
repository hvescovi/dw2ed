from ZODB import FileStorage,DB
import transaction
from c_pessoa import Pessoa

storage = FileStorage.FileStorage('dados/meubd.fs')
db=DB(storage)
connection=db.open()
root=connection.root()

p = Pessoa()
p.nome = "Maria Oliveira"
p.email = "maliv@mail.com"
p.peso = 65

# reassociação
# https://zodb.org/en/latest/articles/ZODB1.html#a-complete-example
pessoas = root['pessoas']
pessoas.append(p)
root['pessoas'] = pessoas

# execuções repetidas deste código vai inserir
# Maria várias vezes no BD

transaction.commit()

print(root.items)

# percorrer as pessoas
for pe in root['pessoas']:
    print(pe)

connection.close()