# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# docker run --name=test-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=testando -d -e MYSQL_ROOT_HOST=% mysql/mysql-server:5.7
# docker run --name myadmin -d --link test-mysql:db -p 8080:80 phpmyadmin/phpmyadmin

# configurações
app = Flask(__name__)
#path = os.path.dirname(os.path.abspath(__file__)) # sugestao do Kaue
#arquivobd = os.path.join(path, 'ex2.db')
# mysql: conectar com 127.0.0.1
# https://stackoverflow.com/questions/18150858/operationalerror-2002-cant-connect-to-local-mysql-server-through-socket-v
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:testando@127.0.0.1:3306/legal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

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
    id = db.Column(db.Integer, db.ForeignKey('foo.id', ondelete="CASCADE"), primary_key=True)

    tamanho_bar = db.Column(db.String(10))

    __tablename__ = 'bar'
    __mapper_args__ = {
        'polymorphic_identity': 'bar',
    }
    def __str__(self):
        return str(self.id)+", "+self.nome+", "+self.tamanho_bar


# início do programa de testes
#if os.path.exists(arquivobd): # se o arquivo já existe...
#    os.remove(arquivobd) # ... o arquivo é removido

#db.session.execute("PRAGMA foreign_keys=ON");
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