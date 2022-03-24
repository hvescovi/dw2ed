class Pai:
    def __init__(self, nome="", email="", telefone=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.filhos = [] # lista reversa inicialmente vazia

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}'

class Filho:
    def __init__(self, nome="", pai=None):
        self.nome = nome
        if pai is None:
            raise Exception("Não pode haver filho sem pai")
        self.pai = pai
    def __str__(self):
        return f'{self.nome}, filho de: {self.pai}'
        

        
# teste da classe
if __name__ == "__main__":
    p1 = Pai(nome = "Pedro", email = "pe@gmail.com", 
        telefone = "47 99012 3232")
    print(p1)
    f1 = Filho(nome="João", pai=p1)
    print(f1)
    f2 = Filho(nome="Maria", pai=p1)
    print(f2)
        
    # adicionar filhos ao pai - lista reversa
    p1.filhos = [f1, f2]

    # exibir TUDO
    print("TODAS as informações:")
    print(p1)
    for f in p1.filhos:
        print(f' Filho: {str(f)}')