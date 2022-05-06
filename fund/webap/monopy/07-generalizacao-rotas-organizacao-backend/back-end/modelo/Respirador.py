class Respirador(db.Model):
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