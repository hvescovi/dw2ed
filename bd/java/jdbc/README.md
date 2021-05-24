* Executando aplicação JDBC no Eclipse
Exemplos do capítulo 19 (Packages) do livro dos Deitel, 10 edição

Na pasta prints há screenshots das telas de configuração do projeto no Eclipse.

Driver do mysql obtido em:
https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.25

Javafx obtido em:
https://gluonhq.com/products/javafx/

No projeto do eclipse, as bibliotecas foram importadas da pasta javafx descompactada em /Downloads. Foram também adicionados parâmetros na execução do projeto, conforme:
https://stackoverflow.com/questions/52144931/how-to-add-javafx-runtime-to-eclipse-in-java-1

Passos da execução:

a) execução do mysql via docker:

$ docker run --name=test-mysql -e MYSQL_ROOT_PASSWORD=testando -e MYSQL_ROOT_HOST=% mysql/mysql-server:5.7

b) acessando o container e populando a base:

$ docker exec -it test-mysql bash

# mysql -u root -p 

mysql> create database ElectricalStore;
mysql> use ElectricalStore;
mysql> create table products (serialNumber char(25), make char(10), description char(25), price decimal(10, 2));
mysql> insert into products values ("1076543", "Acme", "Aspirador de po", 180.11);
mysql> insert into products values ("3756354", "Nadir", "Maquina de lavar", 178.97);
mysql> select * from products;
mysql> help;
mysql> status;
mysql> exit

c) após gerar o .JAR no eclipse (File > Export > select "Java" > Runnable Jar File), segue o comando da execução (é preciso incluir configurações de execução do javafx):

$ java --module-path /home/friend/Downloads/javafx-sdk-11.0.2/lib --add-modules=javafx.controls -jar jdbc_runnable.jar

(2.3MB in the not runnable jar)
(10.2MB in the runnable jar)

FIM