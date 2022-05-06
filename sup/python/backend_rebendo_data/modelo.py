from config import *
from datetime import date

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    mensagem = db.Column(db.Text) # mensagem da pessoa, filosofia
    dtnasc = db.Column(db.Date)
    peso = db.Column(db.Float)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        s = f'{self.id}, {self.nome}, {self.mensagem}, '
        s += f'{self.dtnasc}, {self.peso}'
        # exibindo data de nascimento por partes
        s += f' | {self.dtnasc.day}/{self.dtnasc.month}/{self.dtnasc.year}'
        return s

if __name__ == "__main__": # teste da classe
    if os.path.exists(arquivobd): # apagar o arquivo, se houver
        os.remove(arquivobd)

    db.create_all() # criar tabelas
    
    p = Pessoa(nome = "João da Silva", # teste da classe Pessoa
               mensagem = "Viva o momento e faça planos", 
               dtnasc = date(2014, 1, 25),
               peso = 73.5) 

    db.session.add(p) # persistir
    db.session.commit()
    
    print(p) # exibir a pessoa