JDBC - Capítulo 24 do livro do Deitel

iniciando o servidor de banco de dados MySql com docker:
$ docker run --name=test-mysql -e MYSQL_ROOT_PASSWORD=testando -e MYSQL_ROOT_HOST=% mysql/mysql-server:5.7

iniciando o phpmyadmin:
$ docker run --name myadmin -d --link test-mysql:db -p 8080:80 phpmyadmin/phpmyadmin

login no phpmyadmin (navegador web):
http://localhost:8080

usuario = root
senha = testando



ALTER TABLE AuthorISBN ADD CONSTRAINT pkAuthorISBN PRIMARY KEY (AuthorID, ISBN)
ALTER TABLE AuthorISBN ADD FOREIGN KEY (AuthorID) REFERENCES Authors (AuthorID);
ALTER TABLE AuthorISBN ADD FOREIGN KEY (ISBN) REFERENCES Titles (ISBN)

