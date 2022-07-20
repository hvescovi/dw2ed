from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "pessoas.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{arquivobd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    nome_foto = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.nome_foto
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "nome_foto": self.nome_foto
        }

@app.route("/")
def padrao():
    return "backend ok"

@app.route("/criar_tabelas")
def criar():
    db.create_all()
    return "tabelas criadas"

@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        print("comecando")
        file_val = request.files['foto']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(caminho, 'imagens/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado":"erro", "detalhes": str(e)})

    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

@app.route('/get_image/<int:id_pessoa>')
def get_image(id_pessoa):
    livro = db.session.query(Pessoa).get(id_pessoa)
    arquivoimg = os.path.join(caminho, 'imagens/'+ livro.nome_foto)
    return send_file(arquivoimg, mimetype='image/gif')
       
@app.route("/incluir_pessoa", methods=['post'])
def incluir_pessoa():
    resposta = jsonify({"resultado": "ok", "detalhes": "oi"})
    dados = request.get_json(force=True)
    try:
      nova = Pessoa(**dados)
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e:
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/retornar_pessoas")
def retornar_pessoas():
    try:
        pessoas = db.session.query(Pessoa).all()
        pessoas_em_json = [ x.json() for x in pessoas ]
        retorno = {'resultado': 'ok'}
        retorno.update({'detalhes': pessoas_em_json}) # concatenar dois json's (dicionários)
        resposta = jsonify(retorno)
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)
