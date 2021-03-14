class Aplicativo:
  def __init__(self, nome="", descricao="", autor=""):
    self.nome = nome
    self.descricao = descricao
    self.autor = autor
  def __str__(self):
    return f'''Nome: {self.nome}, 
descrição: {self.descricao}
autor: {self.autor}'''