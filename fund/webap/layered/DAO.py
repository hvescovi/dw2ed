import json
from modelo import Pessoa

caminho = '/home/friend/01-github/dw2ed/fund/webap/layered/'
arquivo = 'dados.json'

def retornarPessoas():
    
    # inicialização padrão
    retorno = []

    try:
        # ler o arquivo json
        pessoas = json.load(open(caminho+arquivo))

        # converter para lista de objetos
        for p in pessoas:
            nova = Pessoa(p['nome'], p['email'], p['telefone'])
            retorno.append(nova)        
    except:
        pass

    # retornar
    return retorno

def incluirPessoa(novaPessoa):

    # padrão
    pessoas = []
    try:
        # ler o arquivo json
        f = open(caminho + arquivo)
        tmp = json.load(f)
        for p in tmp:
            x = p['nome']
            nova = Pessoa(x, p['email'], p['telefone'])
            pessoas.append(nova.json())     
    except Exception as e:
        print("Criando arquivo...") # pass #print(e)

    # incluir a pessoa 
    pessoas.append(novaPessoa.json())

    # persistir o novo arquivo
    with open(caminho+arquivo, 'w') as outfile:
        outfile.write(json.dumps(pessoas))

if __name__ == "__main__":
    # teste da classe DAO
    pessoas = retornarPessoas()
    for p in pessoas:
        print(p)