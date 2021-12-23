if __name__ == "__main__":
  # configuração para permitir importação de arquivos do diretório superior
  # https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/
  import os, sys
  currentdir = os.path.dirname(os.path.realpath(__file__)) # /home/friend/01-github/dw2ed/fund/python/pacote/ex5/classes
  parentdir = os.path.dirname(currentdir) # /home/friend/01-github/dw2ed/fund/python/pacote/ex5
  sys.path.append(parentdir)
  
from classes.pessoa import Pessoa
from classes.celular import Celular

def run():
  print("* Teste da classe Celular")
  joao = Pessoa("João", 70) # instancia uma pessoa 
  s5 = Celular("Samsung S5", 4, joao) # instancia um celular
  print(s5) # exibe o celular e o seu proprietário

if __name__ == "__main__":
  run()