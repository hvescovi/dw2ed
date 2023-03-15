from classes.pessoa import Pessoa
#from classes import pessoa
#import classes - NÃO FUNCIONA. Por que? Veja ex7

def run():
  print("Teste da classe Pessoa")
  joao = Pessoa("João", 70)
  maria = Pessoa("Maria", 130)
  #joao = pessoa.Pessoa("João", 70)
  #maria = pessoa.Pessoa("Maria", 130)
  print(joao)
  print(maria)