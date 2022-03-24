class Quarto:
    def __init__(self, nome="", dimensoes="", casa=None):
        self.nome = nome
        self.dimensoes = dimensoes
        if casa is None: # composicao
            raise Exception("Um quarto deve ser criado em uma casa!")        
        self.casa = casa 
        self.mobilias = [] # lista reversa
    def __str__(self):
        s = f'Quarto: {self.nome}, {self.dimensoes}, em: {str(self.casa)}'
        if self.mobilias:
            s += ", possui mobília(s): "
            for m in self.mobilias:
                s += f'{m.nome}, {m.funcao}, {m.material}, ' 
            s = s[:-2] # remove a última vírgula e espaço
            
        return s
        
class Mobilia:
    def __init__(self, nome="", funcao="", material="", quarto=None):
        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.quarto = quarto
    def __str__(self): # expressão do objeto em forma textual
        s = f'Mobília: {self.nome}, '+\
               f'{self.funcao}, {self.material}'
        if self.quarto:
            s += f', localizada em: {str(self.quarto)}'
        return s

class Casa:
    def __init__(self, formato="", quartos=[]):
        self.formato=formato
        self.quartos = []
        # self.quartos=quartos ==> mapeamento reverso: mantém a lista 
        # inicialmente vazia (sem associar parâmetro), pois casa faz parte de quarto, 
        # não dá pra criar simultaneamente casa com lista de quartos da casa
    def __str__(self):
        s = f'Casa: {self.formato}'
        for quarto in self.quartos:
            s += f', possui quarto(s): {quarto.nome}, {quarto.dimensoes}'
        return s        

if __name__ == "__main__": # teste das classes
    
    c1 = Casa(formato="Germânica")
    print(c1)    
    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    print(q1)
    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)
    print(q2)

    c1.quartos=[q1,q2] # preenche o mapeamento reverso
    print(c1)

    m1 = Mobilia(nome = "Armário", funcao = "Guardar coisas", 
        material = "Madeira", quarto=q1) # quarto é opcional
    print(m1)

    q1.mobilias = [m1] # preenche o mapeamento reverso
    print(q1)
    
    print("*** TESTE com todos os dados")
    print(c1) # exibe a casa e tudo o que há dentro dela      