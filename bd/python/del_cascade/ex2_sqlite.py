# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# https://stackoverflow.com/questions/2614984/sqlite-sqlalchemy-how-to-enforce-foreign-keys
from sqlalchemy.engine import Engine
from sqlalchemy import event


# configurações
app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__)) # sugestao do Kaue
arquivobd = os.path.join(path, 'ex2_sqlite.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

# comando mágico necessário a partir do python 10
app.app_context().push()

class Foo(db.Model):

    id = db.Column(
        db.Integer, 
        db.Sequence('foo_id_seq', start=1001, increment=1),
        primary_key=True
    )
    nome = db.Column(db.String(50))
    discriminator = db.Column('type', db.String(20), nullable=False)


    __tablename__ = 'foo'
    __mapper_args__ = {
        'polymorphic_on': discriminator,
        'polymorphic_identity': 'foo',
    }
    def __str__(self):
        return str(self.id)+", "+self.nome

class Bar(Foo):
    # https://stackoverflow.com/questions/23752892/sqlalchemy-deleting-in-multitable-polymorphism
    # https://stackoverflow.com/questions/47216677/sqlalchemy-joined-inheritance-fast-bulk-deletion-of-child-objects
    id = db.Column(db.Integer, db.ForeignKey('foo.id', ondelete="CASCADE"), primary_key=True)

    tamanho_bar = db.Column(db.String(10))

    __tablename__ = 'bar'
    __mapper_args__ = {
        'polymorphic_identity': 'bar',
    }
    def __str__(self):
        return str(self.id)+", "+self.nome+", "+self.tamanho_bar


# início do programa de testes
if os.path.exists(arquivobd): # se o arquivo já existe...
    os.remove(arquivobd) # ... o arquivo é removido

#db.session.execute("PRAGMA foreign_keys=ON");
#db.session.execute('pragma foreign_keys=on')
#db.session.commit()


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

db.create_all() # criar as tabelas no banco

f1 = Foo(nome = "primeiro foo")
db.session.add(f1)
db.session.commit()

f2 = Foo(nome = "segundo foo")
db.session.add(f2)
db.session.commit()

b1 = Bar(nome = "pessoa 3", tamanho_bar = "cinquenta")
db.session.add(b1)
db.session.commit()

print("AAA")
for f in db.session.query(Foo).all():
    print(f)   
for b in db.session.query(Bar).all():
    print(b)

db.session.query(Foo).filter(Foo.id==1).delete()

print("BBB")
for f in db.session.query(Foo).all():
    print(f)   
for b in db.session.query(Bar).all():
    print(b)   

db.session.query(Foo).filter(Foo.id==3).delete()

print("CCC")
for f in db.session.query(Foo).all():
    print(f)   
for b in db.session.query(Bar).all():
    print(b)   

db.session.commit()