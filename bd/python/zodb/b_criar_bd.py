from ZODB import FileStorage,DB
import transaction

storage = FileStorage.FileStorage('dados/meubd.fs')
db=DB(storage)
connection=db.open()
root=connection.root()

print("banco de dados criado")