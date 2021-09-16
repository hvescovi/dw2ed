# importações
from flask import Flask, jsonify # preparar resposta HTTP no formato json
from flask_sqlalchemy import SQLAlchemy
import os

# configurações
app = Flask(__name__)
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__)) # sugestao do Kaue
arquivobd = os.path.join(path, 'pessoas.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

class Pessoa(db.Model):

    id = db.Column(
        db.Integer, 
        db.Sequence('foo_id_seq', start=1001, increment=1),
        primary_key=True
    )
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(50))

    discriminator = db.Column('type', db.String(20), nullable=False)
    __tablename__ = 'pessoa' # comando opcional
    __mapper_args__ = {
        'polymorphic_on': discriminator,
        'polymorphic_identity': 'pessoa',
    }
    def __str__(self):
        return f'{self.id}, {self.nome}, {self.telefone}'
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "telefone":self.telefone
        }

class Vendedor(Pessoa):
    # https://stackoverflow.com/questions/23752892/sqlalchemy-deleting-in-multitable-polymorphism
    # https://stackoverflow.com/questions/47216677/sqlalchemy-joined-inheritance-fast-bulk-deletion-of-child-objects
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id', ondelete="CASCADE"), primary_key=True)

    matricula = db.Column(db.String(50))

    __tablename__ = 'vendedor'
    __mapper_args__ = {
        'polymorphic_identity': 'vendedor',
    }
    def __str__(self):
        return super().__str__() + f', {self.matricula}'
    def json(self):
        json1 = super().json()
        json2 = json1.update({"matricula":self.matricula})

p1 = Pessoa(nome = "Joao da Silva", telefone = "47 9 9239 2342")
v1 = Vendedor(nome = "Maria de Oliveira", 
              telefone = "47 9 8842 1243",
              matricula = "132346")
print(v1.json())
'''
@app.route("/")
def inicio():
    p1 = Pessoa(nome = "Joao da Silva", telefone = "47 9 9239 2342")
    v1 = Vendedor(nome = "Maria de Oliveira", 
                  telefone = "47 9 8842 1243",
                  matricula = "132346")
                      
    return v1.json()

app.run(debug=True)        

'''
'''
resultado da execução:
$ curl localhost:5000



'''