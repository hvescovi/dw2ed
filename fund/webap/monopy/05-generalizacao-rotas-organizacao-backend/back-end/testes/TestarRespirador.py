from geral.config import *
from modelo.Pessoa import Pessoa
from modelo.Respirador import Respirador

def run():
  print("TESTE DE RESPIRADOR")

  p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
      telefone = "47 99012 3232")
  db.session.add(p1)
  db.session.commit()

  r1 = Respirador(codigo="001A", data_aquisicao="24/03/2020")
  db.session.add(r1)
  db.session.commit()
  print(r1)

  r2 = Respirador(codigo="002B", data_aquisicao="01/02/2020", pessoa = p1, data_emprestimo="04/02/2020")
  db.session.add(r2)
  db.session.commit()
  print(r2)