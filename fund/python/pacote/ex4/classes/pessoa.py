if __name__ == "__main__":
  # configuração para permitir importação de arquivos do diretório superior
  # https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/
  # isso é uma adaptação que pode ser usada enquanto estamos aprendendo
  # daria pra executar o import no próprio programa, sem 
  # necessitar da chamada por um programa "em nível superior" que conheça
  # a estrutura
  # depois de aprender isso, é melhor não usar :-) e usar da forma correta:
  # o programa de nível superior chamando os de nível subordinado
  import os, sys
  currentdir = os.path.dirname(os.path.realpath(__file__)) # /home/friend/01-github/dw2ed/fund/python/pacote/ex4/classes
  parentdir = os.path.dirname(currentdir) # /home/friend/01-github/dw2ed/fund/python/pacote/ex4
  sys.path.append(parentdir)

import config 

class Pessoa:
  def __init__(self, nome="", idade=0):
    self.nome = nome
    if idade > config.IDADE_MAXIMA:
      self.idade = config.IDADE_MAXIMA
    else:
      self.idade = idade
  def __str__(self):
    return f'''Nome: {self.nome}, idade: {self.idade}'''

if __name__ == "__main__":
  joao = Pessoa("João", 70)
  maria = Pessoa("Maria", 130)
  print(joao)
  print(maria)
  # resultado da execução:
  '''
  Nome: João, idade: 70
  Nome: Maria, idade: 120
  '''