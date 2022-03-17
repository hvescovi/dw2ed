class Quarto:
    def __init__(self, nome="", dimensoes=""):
        self.nome = nome
        self.dimensoes = dimensoes
    def __str__(self):
        return f'Quarto: {self.nome}, {self.dimensoes}'

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
    def __init__(self, formato="", quartos=None):
        self.formato=formato
        if quartos is None: # regra da composição
            raise Exception("Uma casa precisa ter pelo menos um quarto")
        self.quartos=quartos
    def __str__(self):
        s = f'Casa: {self.formato}'
        for quarto in self.quartos:
            s += f', possui: {str(quarto)}'
        return s

if __name__ == "__main__": # teste das classes
    
    q1 = Quarto(nome="Sala", dimensoes="6x5 metros")
    print(q1)

    m1 = Mobilia(nome = "Armário", funcao = "Guardar coisas", 
        material = "Madeira", quarto=q1) # quarto é opcional
    print(m1)

    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros")
    c1 = Casa(formato="Germânica", quartos=[q1,q2])
    print(c1)