# importa todos os testes disponíveis, e
# declarados no __init__ da pasta/pacote teste
from teste import * 

# executa os testes
teste_Pessoa.run()
teste_Fabricante.run()
teste_Aplicativo.run()
teste_Celular.run()

# resultado da execução
'''
* Teste da classe Pessoa
Nome: João, idade: 70
Nome: Maria, idade: 120
* Teste da classe Fabricante
Nome: Samsung, 
endereço: Av. dos Oitis, nº 1.460, Distrito Industrial, Manaus/AM, 69.007-002
CNPJ: 00.280.273/0001-37
* Teste da classe Aplicativo
Nome: WhatsApp, 
descrição: Envie mensagens em texto, fotos e vídeos para seus amigos
autor: WhatsApp LLC
* Teste da classe Celular
Modelo: Samsung S5, 
memoria: 4 GB, 
dono: Nome: João, idade: 70,
fabricante: Nome: Samsung, 
endereço: Av. dos Oitis, n 1.460, Distrito Industrial, Manaus/AM, 69.007-002
CNPJ: 00.280.273/0001-37,
aplicativos: 
=> Nome: WhatsApp, 
descrição: Envie mensagens em texto, fotos e vídeos para seus amigos
autor: WhatsApp LLC
=> Nome: Afinador e Metrônomo, 
descrição: Afinador de instrumentos e metrônomo
autor: Soundcorset
'''