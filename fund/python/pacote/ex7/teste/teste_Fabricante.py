from classes.fabricante import Fabricante

def run():
  print("* Teste da classe Fabricante")
  sam = Fabricante("Samsung", "Av. dos Oitis, nº 1.460, "+\
    "Distrito Industrial, Manaus/AM, 69.007-002", 
    "00.280.273/0001-37")
  print(sam) # exibe o celular e o seu proprietário