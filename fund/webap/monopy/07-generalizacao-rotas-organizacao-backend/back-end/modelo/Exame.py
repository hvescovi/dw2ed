class Exame(db.Model):
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