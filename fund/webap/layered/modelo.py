import json

class Pessoa:

    def __init__(self, nome="", email="", telefone=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return self.nome + ", " +\
            self.email + ", " + self.telefone

    def json(self):
        return json.dumps({
            "nome":self.nome,
            "email":self.email,
            "telefone":self.telefone
        })

# teste    
if __name__ == "__main__":
    # teste da classe Pessoa
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99018 3232")
    print(p1)
    print(p1.json())