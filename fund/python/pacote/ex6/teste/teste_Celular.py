from classes.pessoa import Pessoa
from classes.celular import Celular

def run():
  print("* Teste da classe Celular")
  joao = Pessoa("João", 70) # instancia uma pessoa 
  s5 = Celular("Samsung S5", 4, joao) # instancia um celular
  print(s5) # exibe o celular e o seu proprietário