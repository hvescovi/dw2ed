from flask import Flask, jsonify, request, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "pessoa.db")
db= SQLAlchemy(app)

class Pessoa(db.Model):
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

@app.route("/")
def padrao():
    return "backend ok"

@app.route("/criar_tabelas")
def padrao():
    db.create_all()
    return "tabelas criadas"

@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        file_val = request.files['capa']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(caminho, 'imagens/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado":"ok", "detalhes": str(e)})

    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

@app.route('/get_image/<int:id_livro>')
def get_image(id_livro):
    livro = db.session.query(Biblioteca).get(id_livro)
    arquivoimg = os.path.join(caminho, 'imagens/'+ livro.Capa_do_livro)
    # arquivoimg = os.path.join('/home/ingguk/mysite/img_pet', livro.foto)
    # /home/ingguk/mysite/img_pet
    return send_file(arquivoimg, mimetype='image/gif')
       
app.run(debug=True)
