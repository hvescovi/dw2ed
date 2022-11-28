#import config
#import config as c
#from config import IDADE_MAXIMA
from config import *

class Pessoa:
  def __init__(self, nome="", idade=0):
    self.nome = nome
    #if idade > config.IDADE_MAXIMA:
    #if idade > c.IDADE_MAXIMA:
    if idade > IDADE_MAXIMA:
      #self.idade = config.IDADE_MAXIMA
      self.idade = IDADE_MAXIMA
      #self.idade = c.IDADE_MAXIMA
    else:
      self.idade = idade
  def __str__(self):
    return f'''Nome: {self.nome}, idade: {self.idade}'''

joao = Pessoa("João", 70)
maria = Pessoa("Maria", 130)
print(joao)
print(maria)
# resultado da execução:
'''
Nome: João, idade: 70
Nome: Maria, idade: 120
'''