class Pessoa:
    def __init__(self, nome="", email="", telefone=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}'


def test_pessoa():

    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
        
    assert str(p1) == "João da Silva, josilva@gmail.com, 47 99012 3232"