from ZODB import FileStorage,DB
import transaction
from c_pessoa import Pessoa

storage = FileStorage.FileStorage('dados/meubd.fs')
db=DB(storage)
connection=db.open()
root=connection.root()

# has_key foi removido no python 3
# https://stackoverflow.com/questions/33727149/dict-object-has-no-attribute-has-key

if "pessoas_com_chave" not in root.keys():
    root["pessoas_com_chave"] = {}
pchave=root["pessoas_com_chave"]

p = Pessoa() # aqui começou uma transação
p.nome = "João da Silva"
p.email = "josilva@mail.com"
p.peso = 70

if p.nome not in pchave.keys():
    print(p.nome + " já está cadastrado, não vou inserir novamente")
    transaction.abort()
else:
    transaction.commit()
    print(p.nome + " FOI cadastrado") 

connection.close()