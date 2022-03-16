# Exemplo de sistema em camadas, com camada mock (DAO memória)

Plataforma de execução: Eclipse

# Biblioteca json
* Obtenha a biblioteca javax.json-1.1.4 no site: search.maven.org.
O arquivo se encontra atualmente neste endereço: https://repo1.maven.org/maven2/org/glassfish/javax.json/1.1.4/javax.json-1.1.4.jar
(também foi disponibilizado no próprio diretório deste projeto)
* Será necessário alterar as propriedades do projeto para localizar a biblioteca no local correto do seu computador: Eclipse > clique do botão direito no nome do projeto > Propriedades > Java Build Path > Libraries > selecione Classpath > Add External Jar... e aí adiciona o arquivo .jar do json.

# Teste
* No programa TestarPessoaDAO, altere o import para usar o DAO em memória, e depois usar o DAO em json.
* Na tela de pessoas, faça também essas alterações de importação para verificar o uso da camada DAO em memória e o uso o DAO json.

Enquanto estiver executando o DAO json, o arquivo json fica no diretório temporário (c:\temp para windows, /tmp/ para linux)