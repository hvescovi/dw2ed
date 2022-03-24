from config import *

class Casa (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formato = db.Column(db.String(254))

    # lista reversa
    #quartos = db.relationship("Quarto", backref="quartos")
    
    def __str__(self):
        s = f'Casa: {self.formato}'
     #   for quarto in self.quartos:
      #      s += f', possui quarto(s): {str(quarto)}'
        return s        

class Quarto(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    dimensoes = db.Column(db.String(254))

    casa_id = db.Column(db.Integer, db.ForeignKey(Casa.id), 
                          nullable=False)
    casa = db.relationship("Casa")

    # lista reversa
    casas = db.relationship("Casa", backref="quartos")
       
    def __str__(self):
        s = f'Quarto: {self.nome}, {self.dimensoes}, em: {str(self.casa)}'
        s += f'na casa: {self.casa.formato}'          
        return s

if __name__ == "__main__": # teste das classes
    
    c1 = Casa(formato="Germânica")
    print(c1)    
    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    print(q1)
    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)
    print(q2)

    #c1.quartos=[q1,q2] # preenche o mapeamento reverso
    print(c1)
    
    #q1.mobilias = [m1] # preenche o mapeamento reverso
    print(q1)
    
    print("*** TESTE com todos os dados")
    print(c1) # exibe a casa
    for q in db.session.query(Quarto).filter(c1.id=Quarto.casa_id).all()
        print(q)
    