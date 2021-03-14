if __name__ == "__main__":
  # configuração para permitir importação de arquivos do diretório superior
  import os, sys
  atual = os.path.abspath(".") #  retorna o diretório superior
  sys.path.append(atual) # inclui esse diretório no path (caminhos conhecidos)

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