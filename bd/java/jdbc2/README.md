Exemplo de JDBC - capítulo 24 do livro do Deitel

Projeto criado no Eclipse

Necessita do driver mysql:
https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.25

Iniciando o servidor de banco de dados MySql com docker:
$ docker run --name=test-mysql -e MYSQL_ROOT_PASSWORD=testando -e MYSQL_ROOT_HOST=% mysql/mysql-server:5.7

Iniciando o phpmyadmin:
$ docker run --name myadmin -d --link test-mysql:db -p 8080:80 phpmyadmin/phpmyadmin

Login no phpmyadmin (navegador web):
http://localhost:8080
usuario = root
senha = testando

Além dos comandos de criação de tabelas, foram executados também estes comandos:

ALTER TABLE AuthorISBN ADD CONSTRAINT pkAuthorISBN PRIMARY KEY (AuthorID, ISBN)

ALTER TABLE AuthorISBN ADD FOREIGN KEY (AuthorID) REFERENCES Authors (AuthorID)

ALTER TABLE AuthorISBN ADD FOREIGN KEY (ISBN) REFERENCES Titles (ISBN)

O script de geração do BD está disponível em um arquivo .sql.