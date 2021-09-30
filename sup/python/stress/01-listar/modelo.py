from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.email + ", " + self.telefone
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # inserção de muitos registros
    for i in range(0,10000):
        n = names.get_full_name()
        em = n.strip() + "@gmail.com"
        tel = "9" + str(random.randint(8,9))
        for i in range(1,7):
            tel += str(random.randint(1,9))
        p1 = Pessoa(nome = n, email = em, telefone = tel)
        db.session.add(p1)
        
    db.session.commit()
    
    for p in db.session.query(Pessoa).all():
        print(p)

# no linux: 
# $ time python3 modelo.py (para verificar tempo de execução)        
# $ top (para acompanhar esforço de CPU)
# stress do backend:
# for i in {1..10}; do ./vai.sh; done
# vai.sh: curl localhost:5000/listar_pessoas &
# bibliotecas: names e random