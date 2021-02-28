import config.param as c

class Pessoa:
  def __init__(self, nome="", idade=0):
    self.nome = nome
    if idade > c.IDADE_MAXIMA:
      self.idade = c.IDADE_MAXIMA
    else:
      self.idade = idade
  def __str__(self):
    return f'''
    Nome: {self.nome},
    idade: {self.idade}
    '''