class Quarto:
    def __init__(self, nome="", dimensoes="", casa=None):
        self.nome = nome
        self.dimensoes = dimensoes
        if casa is None: # composicao
            raise Exception("Um quarto deve ser criado em uma casa!")        
        self.casa = casa         
    def __str__(self):
        return f'Quarto: {self.nome}, {self.dimensoes}, em: {str(self.casa)}'

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
    def __init__(self, formato=""):
        self.formato=formato
    def __str__(self):
        s = f'Casa: {self.formato}'
        return s

if __name__ == "__main__": # teste das classes
    
    c1 = Casa(formato="Germânica")
    print(c1)

    q1 = Quarto(nome="Sala", dimensoes="6x5 metros", casa=c1)
    print(q1)

    m1 = Mobilia(nome = "Armário", funcao = "Guardar coisas", 
        material = "Madeira", quarto=q1) # quarto é opcional
    print(m1)

    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros", casa=c1)
    print(q2)
    
    # percorrendo e listando
    