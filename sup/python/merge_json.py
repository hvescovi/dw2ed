from flask import Flask, jsonify

app = Flask(__name__)

# definir 2 conteúdos json
json1 = {
    "nome":"João da Silva",
    "telefone":"47 9 9212 0212"
}
print(json1)
json2 = {
    "email":"josilva@gmail.com"

}

# fazer a junção de 2 conteúdos json
json1.update(json2)

print(json1)

@app.route("/")
def inicio():
    return jsonify(json1)

app.run(debug=True)        
'''
resultado da execução:
$ curl localhost:5000
{
  "email": "josilva@gmail.com", 
  "nome": "Jo\u00e3o da Silva", 
  "telefone": "47 9 9212 0212"
}
'''

