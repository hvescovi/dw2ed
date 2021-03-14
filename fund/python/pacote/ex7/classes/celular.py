class Celular:
  def __init__(self, modelo="", memoria=4, dono=None, 
               fabricante=None, aplicativos=None):
    self.modelo = modelo
    self.memoria = memoria
    self.proprietario = dono
    self.fabricante = fabricante
    self.aplicativos = aplicativos
  def __str__(self):
    apps = ""
    for app in self.aplicativos: # percorrer os aplicativos
      apps += "\n=> " + str(app) # veja: aqui usa o método str
    return f'''Modelo: {self.modelo}, 
memoria: {self.memoria} GB, 
dono: {str(self.proprietario)},
fabricante: {str(self.fabricante)}, # comando str aqui também ;-)
aplicativos: {apps}'''