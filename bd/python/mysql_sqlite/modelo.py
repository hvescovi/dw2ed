from configuracoes import *

class Pessoa(db.Model):
    __tablename__ = 'hylson_sqlalchemy_pessoa'
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.telefone
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

class Exame(db.Model):
    __tablename__ = 'hylson_sqlalchemy_exame'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254)) # nome do exame
    unidade = db.Column(db.String(254)) # unidade de medida
    vr = db.Column(db.String(254)) # valores de referência
    def __str__(self):
        return f"{self.nome} [{self.id}], unidade={self.unidade} ({self.vr})"  
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "unidade":self.unidade,
            "vr":self.vr
        }
    
class ExameRealizado(db.Model):
    __tablename__ = 'hylson_sqlalchemy_exame_realizado'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(254)) # data do exame
    resultado = db.Column(db.String(254)) # apenas o valor
    
    # pessoa que fez o exame; não pode ser nulo (composição!)
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")
    # exame que foi realizado; não pode ser nulo (composição!)
    exame_id =  db.Column(db.Integer, db.ForeignKey(Exame.id), nullable=False)
    exame = db.relationship("Exame")

    def __str__(self): # expressão da classe em forma de texto
        return f"{self.data}, {self.resultado}, " + \
            f"{self.pessoa}, {self.exame}"

    def json(self):
        return {
            "id":self.id,
            "data":self.data,
            "resultado":self.resultado,
            "pessoa_id":self.pessoa_id,
            "pessoa":self.pessoa.json(),
            "exame_id":self.exame_id,
            "exame":self.exame.json()
        }

class Respirador(db.Model):
    __tablename__ = 'hylson_sqlalchemy_respirador'
    id = db.Column(db.Integer, primary_key=True) # id interno
    codigo = db.Column(db.String(254)) # código do equipamento
    data_aquisicao = db.Column(db.String(254))
    data_emprestimo = db.Column(db.String(254)) # emprestado? se sim, desde quando?

    # atributo de chave estrangeira
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id))
    # atributo de relacionamento, para acesso aos dados via objeto
    pessoa = db.relationship("Pessoa")

    def __str__(self): # expressão da classe em forma de texto
        s = f"Respirador {self.codigo} adquirido em {self.data_aquisicao}"
        if self.pessoa != None:
            s += f", emprestado para {self.pessoa} desde {self.data_aquisicao}"
        return s

    def json(self):
        if self.pessoa is None: # o respirador não está emprestado?
            pessoa_id = ""
            pessoa = ""
            data_emprestimo = ""
        else: # o respirador está emprestado!! :-)
            pessoa_id = self.pessoa_id
            pessoa = self.pessoa.json()
            data_emprestimo = self.data_emprestimo
            
        return {
            "id": self.id,
            "codigo": self.codigo,
            "data_aquisicao": self.data_aquisicao,
            "pessoa_id": pessoa_id,
            "pessoa": pessoa,
            "data_emprestimo": data_emprestimo
        } 