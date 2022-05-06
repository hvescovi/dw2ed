if __name__ == "__main__":
  # configuração para permitir importação de arquivos do diretório superior
  # https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/
  import os, sys
  currentdir = os.path.dirname(os.path.realpath(__file__)) # /home/friend/01-github/dw2ed/fund/webap/monopy/04-composicao/back-end/testes
  parentdir = os.path.dirname(currentdir) # /home/friend/01-github/dw2ed/fund/webap/monopy/04-composicao/back-end/testes
  sys.path.append(parentdir)

from geral.config import *
from modelo.Pessoa import Pessoa

p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
    telefone = "47 99012 3232")
p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
    telefone = "47 98822 2531")        
db.session.add(p1)
db.session.add(p2)
db.session.commit()
print(p1, p2)