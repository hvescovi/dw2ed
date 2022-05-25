from modelo import Pessoa
import DAO

# teste da classe Pessoa
p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
    telefone = "47 99018 3232")

p2 = Pessoa(nome = "Maria Oliveira", email = "maoliv@gmail.com", 
    telefone = "47 98622 1233")

DAO.incluirPessoa(p1)
DAO.incluirPessoa(p2)
print("dados json criados")