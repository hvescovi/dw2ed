class Pessoa:
    def __init__(self, nome="", email="", telefone="", celular=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.celular = celular

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}, '+\
               f'{str(self.celular)}'
class Celular:
    def __init__(self, numero, modelo, chip):
        self.numero = numero
        self.modelo = modelo
        self.chip = chip
    def __str__(self):
        return self.numero + ", "+\
        self.modelo+", "+self.chip

# teste da classe
if __name__ == "__main__":
    c1 = Celular("47-92919293", "motorola", "vivo")
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232", celular=c1)    
    # exibir a pessoa
    print(p1)
