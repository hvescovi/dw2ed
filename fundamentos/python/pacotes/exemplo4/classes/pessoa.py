# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder

if __name__ == "__main__":
  import os
  import sys
  currentdir = os.path.dirname(os.path.realpath(__file__))
  parentdir = os.path.dirname(currentdir)
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
    return f'''
    Nome: {self.nome},
    idade: {self.idade}
    '''

if __name__ == "__main__":
  joao = Pessoa("João", 70)
  maria = Pessoa("Maria", 130)
  print(joao, maria)