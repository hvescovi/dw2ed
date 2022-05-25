import json
from modelo import Pessoa

def retornarPessoas():
    
    # inicialização padrão
    retorno = []

    try:
        # ler o arquivo json
        pessoas = json.load(open('dados.json'))

        # converter para lista de objetos
        for p in pessoas:
            nova = Pessoa(p['nome'], p['email'], p['telefone'])
            retorno.add(nova)        
    except:
        pass

    # retornar
    return retorno

def incluirPessoa(p):

    # padrão
    pessoas = []
    try:
        # ler o arquivo json
        tmp = json.loads(open('dados.json'))
        for p in tmp:
            nova = Pessoa(p['nome'], p['email'], p['telefone'])
            pessoas.add(nova)     
    except:
        pass

    # incluir a pessoa 
    pessoas.append(p)

    # persistir o novo arquivo
    with open('dados.json', 'w') as f:
        for p in pessoas:
            print(p)
            nova = p.json()
            print("escrevendo")
            print(nova)
            f.write(nova)


if __name__ == "__main__":
    # teste da classe DAO
    pessoas = retornarPessoas()
    for p in pessoas:
        print(p)
