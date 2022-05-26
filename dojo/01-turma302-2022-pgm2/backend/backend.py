from config import *
from modelo import Carro

@app.route("/")
def inicio():
    return 'Sitemas de cadastro de carros.'



@app.route("/listar_carros")
def listar_carros():
    carros = db.session.query(Carro).all()
    carros_em_json = [ x.json() for x in carros ]
    r1 = jsonify(carros_em_json)

    r1.headers.add("Access-Control-Allow-Origin", "*")
    return r1
app.run(debug=True)

