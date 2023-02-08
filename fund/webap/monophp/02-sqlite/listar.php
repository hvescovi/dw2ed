<?php
/* 

referências:

https://www.a2hosting.com.br/kb/developer-corner/sqlite/connect-to-sqlite-using-php 
https://www.w3schools.com/php/php_json.asp
https://www.kodingmadesimple.com/2018/01/php-merge-two-json-strings.html
https://zetcode.com/php/sqlite3/

$sudo vim /etc/php/7.4/cli/php.ini
extension=sqlite3
We must enable the sqlite3 extension in the php.ini file.

https://cursos.alura.com.br/forum/topico-php-startup-unable-to-load-dynamic-library-pdo_sqlite-123546

    $ sudo apt install php-sqlite3

*/
?>

<?php
    // conectar ao arquivo do sqlite
    $myPDO = new PDO('sqlite:/home/friend/01-github/dw2ed/fund/webap/monopy/10-sessao-login-front-back/back-end/geral/pessoa.db');

    // fazer a consulta SQL
    $result = $myPDO->query("SELECT * FROM pessoa");

    // percorrer os registros
    foreach($result as $row)
    {
        // obtém array de pessoa
        $pessoa = array("id"=>$row['id'],
                        "nome"=>$row['nome'],
                        "email"=>$row['email'],
                        "telefone"=>$row['telefone']);
        // converte pra json
        $pessoaj = json_encode($pessoa);
        // adiciona essa pessoa json em um array
        $pessoas[] = json_decode($pessoaj, true);

        //print $row['lastname'] . "\n";
    }

    // converte o array de php para json
    $resultado = json_encode($pessoas, JSON_PRETTY_PRINT);

    // retorna/exibe
    echo $resultado;
?>


<?php

/*

- levantar o servidor php:

php -S localhost:8000

- resultado do teste:

$ curl localhost:8000/backend-listar.php

[
    {
        "id": "1",
        "nome": "Tiago",
        "email": "ti@gmail.com",
        "telefone": "123123123"
    },
    {
        "id": "2",
        "nome": "Maria Oliveira",
        "email": "molive@gmail.com",
        "telefone": "47 98822 2531"
    }
]
*/
?>