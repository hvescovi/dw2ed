from Persistence import Persistent

class Pessoa(Persistent):

    def __init__(self):
        self.nome = ""
        self.email = ""
        self.peso = 0

    def __str__(self):
        return f'{self.nome}, {self.email}, {str(self.peso)}'

if __name__=="__main__":
    p = Pessoa()
    p.nome = "João da Silva"
    p.email = "josilva@mail.com"
    p.peso = 70
    print(p)