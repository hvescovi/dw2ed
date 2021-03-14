import config.param as c

class Celular:
  def __init__(self, modelo="", memoria=4, dono=None, fabricante=None):
    self.modelo = modelo
    self.memoria = memoria
    self.proprietario = dono
    self.fabricante = fabricante
  def __str__(self):
    return f'''Modelo: {self.modelo}, 
memoria: {self.memoria} GB, 
dono: {str(self.proprietario)},
fabricante: {str(self.fabricante)}'''