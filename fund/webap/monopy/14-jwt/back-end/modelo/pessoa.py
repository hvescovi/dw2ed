from geral.config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    senha = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.nome} [id={str(self.id)}], ' +\
               f'{self.email}, {self.telefone}, {self.senha}'

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "senha": self.senha
        }