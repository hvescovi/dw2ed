from ZODB import FileStorage,DB
import transaction
from c_pessoa import Pessoa

storage = FileStorage.FileStorage('dados/meubd.fs')
db=DB(storage)
connection=db.open()
root=connection.root()

if not root.has_key("pessoas_com_chave"):
    root["pessoas_com_chave"] = {}
pchave=root["pessoas_com_chave"]

p = Pessoa()
p.nome = "João da Silva"
p.email = "josilva@mail.com"
p.peso = 70

if pchave.has_key(p.nome):
    print(p.nome + " já está cadastrado, não vou inserir novamente")
else:
    print(p.nome + " FOI cadastrado")
    
connection.close()