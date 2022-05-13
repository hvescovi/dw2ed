# from: https://zodb.org/en/latest/articles/ZODB1.html

from ZODB import FileStorage,DB
import transaction

storage = FileStorage.FileStorage('dados/meubd.fs')
db=DB(storage)
connection=db.open()
root=connection.root()

root['employeers'] = ['Mary','Jo','Bob']

transaction.commit()

print(root.items)

connection.close()