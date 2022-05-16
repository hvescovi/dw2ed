class Pessoa:
    def __init__(self, nome="", email="", telefone=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}'

# teste da classe
if __name__ == "__main__":
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
    #p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
    #    telefone = "47 98822 2531")        
    dic = {"nome":"Maria Oliveira", 
           "email":"molive@gmail.com", 
           "telefone":"47 98822 2531"}
    p2 = Pessoa(**dic)
    
    # exibir a pessoa
    print(p2)
    # resultado: Maria Oliveira, molive@gmail.com, 47 98822 2531