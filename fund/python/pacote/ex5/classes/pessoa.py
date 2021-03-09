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