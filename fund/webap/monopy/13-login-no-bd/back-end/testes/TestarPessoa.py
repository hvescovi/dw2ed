from modelo.pessoa import Pessoa
from geral.cripto import *
from geral.config import *

def run():
    print("TESTE DE PESSOA")
    
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
    telefone = "47 99012 3232", senha = cifrar("joao123"))
    p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
        telefone = "47 98822 2531", senha = cifrar("maria456"))        
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    print(p1, p2)