from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def padrao():
    return 'flask web server recebendo parâmetros get, post e json'
    
@app.route('/recebe', methods=['GET','POST'])
def recebe():
    if request.method == 'POST':
        valor = request.form['chave']
        return "Parâmetro recebido via POST: "+valor+"\n"
    elif request.method == 'GET':
        valor = request.args.get('chave')
        return "Parâmetro recebido via GET: "+valor+"\n"

app.run(debug=True)

# teste via curl:
# curl localhost:5000/recebe?chave=12345
# curl -X POST -d 'chave=54321' localhost:5000/recebe