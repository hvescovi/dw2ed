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

        s += f' | {self.dtnasc.day}/{self.dtnasc.month}/{self.dtnasc.year}'
        #for item in vars(self).items():
        #    s += item + ", "
        return s

# teste da classe
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    p = Pessoa(nome = "João da Silva", 
               mensagem = "Viva o momento e faça planos", 
               dtnasc = date(2014, 1, 25),
               peso = 73.5) 

    # persistir
    db.session.add(p)
    db.session.commit()
    
    # exibir a pessoa
    print(p)