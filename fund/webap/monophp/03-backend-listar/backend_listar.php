<?php
/* 

referências:

https://www.a2hosting.com.br/kb/developer-corner/sqlite/connect-to-sqlite-using-php 
https://www.w3schools.com/php/php_json.asp
https://www.kodingmadesimple.com/2018/01/php-merge-two-json-strings.html
https://zetcode.com/php/sqlite3/
https://stackoverflow.com/questions/20286208/merging-two-json-in-php

$sudo vim /etc/php/7.4/cli/php.ini
extension=sqlite3
We must enable the sqlite3 extension in the php.ini file.

https://cursos.alura.com.br/forum/topico-php-startup-unable-to-load-dynamic-library-pdo_sqlite-123546

    $ sudo apt install php7.4-sqlite3

*/
?>

<?php
    // conectar ao arquivo do sqlite
    $myPDO = new PDO('sqlite:/home/friend/01-github/dw2ed/fund/webap/monopy/10-sessao-login-front-back/back-end/geral/pessoa.db');

    // recebe o parâmetro de qual classe listar, via parametrização REST
    // https://codereview.stackexchange.com/questions/85586/rest-api-using-php
    $uri = $_SERVER['PATH_INFO'];
    //print("\n");
    //print($uri);

    // divide por barra
    $partes = explode("/", $uri); // exemplo: /listar/Pessoa
    //print("\n");
    //print($partes);

    // pega a parte 1
    $classe = $partes[2];

    //print("\n");
    //print($classe);

    if ($classe == "Pessoa") 
        $sql = "SELECT * FROM pessoa";
    else 
        echo '{"resultado":"erro", "detalhes":"classe não encontrada: '+$classe+'"}';

    // fazer a consulta SQL
    $result = $myPDO->query($sql);

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

        //print $row['nome'] . "\n";
    }

    // cria dois vetores que serão partes da resposta
    $parte1 = array('resultado' => 'ok');
    $parte2 = array('detalhes' => $pessoas);
    // faz a junção das duas partes
    $tudo = array_merge($parte1, $parte2);
    // transforma em json
    $resposta = json_encode($tudo);
    // retorna/exibe
    echo $resposta;
?>





<?php

/*

- levantar o servidor php:

php -S localhost:8000

- resultado de testes:

$ curl localhost:8000/listar.php/listar/Pessoa

{"resultado":"ok","detalhes":[{"id":"1","nome":"Tiago","email":"ti@gmail.com","telefone":"123123123"},{"id":"2","nome":"Maria Oliveira","email":"molive@gmail.com","telefone":"47 98822 2531"}]}

$ curl localhost:8000/listar.php/listar/Pessoa | json_pp
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   195    0   195    0     0   190k      0 --:--:-- --:--:-- --:--:--  190k
{
   "detalhes" : [
      {
         "email" : "ti@gmail.com",
         "id" : "1",
         "nome" : "Tiago",
         "telefone" : "123123123"
      },
      {
         "email" : "molive@gmail.com",
         "id" : "2",
         "nome" : "Maria Oliveira",
         "telefone" : "47 98822 2531"
      }
   ],
   "resultado" : "ok"
}


?>