from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    exames = db.relationship("ExameRealizado", backref="pessoas")

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        s = self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.telefone  
        return s

class ExameRealizado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254)) # nome do exame
    data = db.Column(db.String(254)) # data do exame
    resultado = db.Column(db.String(254)) # apenas o valor
    
    # pessoa que fez o exame; não pode ser nulo (composição!)
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), 
                          nullable=False)
    pessoa = db.relationship("Pessoa")
        
    def __str__(self): # expressão da classe em forma de texto
        return f"{self.id}) {self.nome}, {self.data}, {self.resultado}, " + \
            f"{str(self.pessoa)}"

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # criar pessoa
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
    db.session.add(p1)
    db.session.commit()
    print(p1)
    
    # criar exames realizados
    e1 = ExameRealizado(nome="Vitamina B12", data="02/02/2020", 
          resultado="219,0 pg/mL", pessoa=p1)
    e2 = ExameRealizado(nome="Vitamina D", data="02/02/2020",
          resultado="44.7 ng/ml", pessoa=p1)
    db.session.add(e1)
    db.session.add(e2)
    db.session.commit()
    print(e1)
    print(e2)

    # mostrando os exames que a pessoa fez - mapeamento reverso
    print(p1)
    s = ""
    for e in p1.exames:
        s += f'{str(e)}, '
    s = s[:-2] # remover vírgula e espaço extras
    print(f'Fez estes exames: {s}')