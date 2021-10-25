from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'(id={self.id}) {self.nome}, '+\
               f'{self.email}, {self.telefone}'

# teste da classe
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
    p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
        telefone = "47 98822 2531")
    p3 = Pessoa(nome = "Joana Tristão", email = "jotristao@gmail.com", 
        telefone = "47 99123 1289")        
    
    # persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.commit()
    
    # localizar uma pessoa por email
    print("Quem tem email molive@gmail.com?")
    alguem = Pessoa.query.filter_by(email='molive@gmail.com').first()
    print(alguem)

    print("Quem tem a expressão 'ri' no nome?")
    pessoas = Pessoa.query.filter(Pessoa.nome.contains('ri'))
    for pessoa in pessoas:
        print(pessoa)

    # localizar uma pessoa pelo ID
    primeira = Pessoa.query.get(1)
    print("Primeira pessoa: " + str(primeira))

    # atualizar os dados de uma pessoa já carregada na memória (em objeto)
    primeira.email = "josilva@hotmail.com" # original = gmail
    db.session.commit()
    print(primeira)

    #Pessoa.query.update({Pessoa.email : Pessoa.email + "(ALTERAR - inválido)"})
    #db.session.commit()

    #update(Pessoa).\
    #    where(Pessoa.email.match("%hotmail%")).\
    #    values({Pessoa.email : Pessoa.email + "(ALTERAR - inválido)"})
    #db.session.commit()

    # exibir as pessoas
    #[print(str(p) for p in db.session.query(Pessoa).all())] 

# referências: 
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
# https://stackoverflow.com/questions/4926757/sqlalchemy-query-where-a-column-contains-a-substring
# https://stackoverflow.com/questions/6750017/how-to-query-database-by-id-using-sqlalchemy