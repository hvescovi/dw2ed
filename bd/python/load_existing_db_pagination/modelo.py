from config import *

# n,name,domain,year founded,industry,
# size range,locality,country,linkedin url,
# current employee estimate,
# total employee estimate

class Compania(db.Model):
    # atributos da pessoa
    id = db.Column('n', db.Integer, primary_key=True)
    nome = db.Column('name',db.String(254))
    dominio = db.Column('domain',db.String(254))
    ano = db.Column('year founded', db.String(254))
    industria = db.Column('industry',db.String(254))
    tamanho = db.Column('size range', db.String(254))
    localizacao = db.Column('locality', db.String(254))
    pais = db.Column('country', db.String(254))
    linkedin = db.Column('linkedin url', db.String(254))
    empregados_atual = db.Column('current employee estimate', db.String(254))
    empregados_total = db.Column('total employee estimate', db.String(254))

# teste da classe
if __name__ == "__main__":

    # exibindo todos os registros
    #n = 1
    #for c in db.session.query(Compania).all():
    #    print(n, c.id, c.nome)
    #    n+=1

    # exibindo apenas 10 registros
    n = 1        
    for c in db.session.query(Compania).limit(10):
        print(n, c.id, c.nome)
        n+=1
    # exibindo apenas registros entre 6 e 8
    n = 1        
    for c in db.session.query(Compania).offset(5).limit(3):
        print(n, c.id, c.nome)
        n+=1