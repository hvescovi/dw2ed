if __name__ == "__main__":
  # configuração para permitir importação de arquivos do diretório superior
  # https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/
  import os, sys
  currentdir = os.path.dirname(os.path.realpath(__file__)) # /home/friend/01-github/dw2ed/fund/python/pacote/ex5/classes
  parentdir = os.path.dirname(currentdir) # /home/friend/01-github/dw2ed/fund/python/pacote/ex5
  sys.path.append(parentdir)
  
from classes.pessoa import Pessoa

def run():
  print("* Teste da classe Pessoa")
  joao = Pessoa("João", 70)
  maria = Pessoa("Maria", 130)
  print(joao)
  print(maria)

if __name__ == "__main__":
  run()