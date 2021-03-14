import config.param as c

class Fabricante:
  def __init__(self, nome="", end="", CNPJ=""):
    self.nome = nome
    self.endereco = end
    self.cnpj = CNPJ
  def __str__(self):
    return f'''Nome: {self.nome}, 
endereço: {self.endereco}
CNPJ: {self.cnpj}'''