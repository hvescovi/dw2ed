# a importação com * remete ao uso do nome do arquivo
# em frente a cada nome da classe
from classes import *

def run():
  print("* Teste da classe Celular")
  joao = pessoa.Pessoa("João", 70) # instancia uma pessoa 
  sam = fabricante.Fabricante("Samsung", "Av. dos Oitis, nº 1.460, "+\
    "Distrito Industrial, Manaus/AM, 69.007-002", 
    "00.280.273/0001-37")
  s5 = celular.Celular("Samsung S5", 4, joao, sam) # instancia um celular
  print(s5) # exibe o celular e o seu proprietário