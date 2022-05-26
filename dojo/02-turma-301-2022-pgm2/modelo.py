import os
from config import *

class Carro(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    ano = db.Column(db.String(254))
    marca = db.Column(db.String(254))
    cor = db.Column(db.String(254))

    def __str__(self) -> str:
        return str(self.id)+")"+ self.ano + "," +\
            self.marca + "," + self.cor

    def json(self):
        return {
            "id" : self.id, 
            "ano" : self.ano,
            "marca" : self.marca,
            "cor" : self.cor
        }    

if __name__ =='__main__':

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    c1 = Carro(ano = "1972", marca = "Ferrari", cor = "vermelha")

    db.session.add(c1)
    db.session.commit()

    print(c1)
    print(f"c1 em json: {c1.json()}")

    

