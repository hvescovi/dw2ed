from geral.config import *
from modelo.Pessoa import Pessoa
from modelo.Exame import Exame

class ExameRealizado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(254)) # data do exame
    resultado = db.Column(db.String(254)) # apenas o valor
    
    # pessoa que fez o exame; não pode ser nulo (composição!)
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")
    # exame que foi realizado; não pode ser nulo (composição!)
    exame_id =  db.Column(db.Integer, db.ForeignKey(Exame.id), nullable=False)
    exame = db.relationship("Exame")

    def __str__(self): # expressão da classe em forma de texto
        return f"{self.data}, {self.resultado}, " + \
            f"{self.pessoa}, {self.exame}"

    def json(self):
        return {
            "id":self.id,
            "data":self.data,
            "resultado":self.resultado,
            "pessoa_id":self.pessoa_id,
            "pessoa":self.pessoa.json(),
            "exame_id":self.exame_id,
            "exame":self.exame.json()
        }
