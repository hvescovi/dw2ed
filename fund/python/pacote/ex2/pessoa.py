#import regras.config
import regras.config as rc

class Pessoa:
  def __init__(self, nome="", idade=0):
    self.nome = nome
    #if idade > regras.config.IDADE_MAXIMA:
    if idade > rc.IDADE_MAXIMA:
    #if idade > regras.config.IDADE_MAXIMA:
      #self.idade = regras.config.IDADE_MAXIMA
      self.idade = rc.IDADE_MAXIMA
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