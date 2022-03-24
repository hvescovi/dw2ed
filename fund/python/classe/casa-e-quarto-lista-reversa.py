class Casa:
    def __init__(self, formato=""):
        self.formato = formato
        self.quartos = [] # lista reversa inicialmente vazia

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.formato}'

class Quarto:
    def __init__(self, nome="", dimensoes="", casa=None):
        self.nome = nome
        self.dimensoes = dimensoes
        if casa is None:
            raise Exception("O quarto precisa ser criado em uma casa")          
        self.casa = casa
    def __str__(self):
        return f'Quarto: {self.nome}, {self.dimensoes}, em: {str(self.casa)}'
             
# teste das classes
if __name__ == "__main__":
    
    c1 = Casa(formato="Germânica")
    print(f'TESTE de casa: {str(c1)}')
        
    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    print(f'TESTE de quarto: {str(q1)}')

    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)
    print(f'TESTE de quarto: {str(q2)}')
        
    # adicionar quartos à casa - lista reversa
    c1.quartos = [q1, q2]

    # exibir TUDO
    print("Teste de TODAS as informações:")
    print(c1)
    for q in c1.quartos:
        print(f' Quarto: {str(q)}')