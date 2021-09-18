import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Sistema de upload"

@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    resposta = jsonify({"mensagem":"tentando..."})
    if request.method == 'POST':
        file_val = request.files['file']
        file_val.save("./"+file_val.filename)
        resposta = jsonify({"mensagem":"ok"})

    return resposta

app.run()