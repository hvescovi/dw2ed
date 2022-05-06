from configuracoes import *
from modelo import *

# criar pessoas
p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
    telefone = "47 99012 3232")
p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
    telefone = "47 98822 2531")        
db.session.add(p1)
db.session.add(p2)
db.session.commit()

# criar exames
b12 = Exame(nome="B12", unidade="pg/mL", vr="239 a 931")
colesterol = Exame(nome="Colesterol total", unidade="mg/dL", 
    vr="menor que 150")

# criar resultado de exame
e1 = ExameRealizado(data="02/02/2020", exame=b12, 
    resultado="219,0 pg/mL", pessoa=p1)
db.session.add(e1)
db.session.commit()
print(f"Exame realizado: {e1}")
print(f"Exame realizado em json: {e1.json()}")
''' resultado:
Exame realizado: 02/02/2020, 219,0 pg/mL, João da Silva[id=1], josilva@gmail.com, 47 99012 3232, B12 [1], unidade=pg/mL (239 a 931)
Exame realizado em json: {'id': 1, 'data': '02/02/2020', 'resultado': '219,0 pg/mL', 'pessoa_id': 1, 'pessoa': {'id': 1, 'nome': 'João da Silva', 'email': 'josilva@gmail.com', 'telefone': '47 99012 3232'}, 'exame_id': 1, 'exame': {'id': 1, 'nome': 'B12', 'unidade': 'pg/mL', 'vr': '239 a 931'}}
RESULTADO JSON FORMATADO (no site https://jsonformatter.curiousconcept.com/):
{
    "id":1,
    "data":"02/02/2020",
    "resultado":"219,0 pg/mL",
    "pessoa_id":1,
    "pessoa":{
    "id":1,
    "nome":"João da Silva",
    "email":"josilva@gmail.com",
    "telefone":"47 99012 3232"
    },
    "exame_id":1,
    "exame":{
    "id":1,
    "nome":"B12",
    "unidade":"pg/mL",
    "vr":"239 a 931"
    }
}
'''
# adicionando alguns respiradores...
r1 = Respirador(codigo="001A", data_aquisicao="24/03/2020")
db.session.add(r1)
db.session.commit()
r2 = Respirador(codigo="002B", data_aquisicao="01/02/2020", pessoa = p1, data_emprestimo="04/02/2020")
db.session.add(r2)
db.session.commit()