<%-- 
    Document   : form
    Created on : Mar 17, 2022, 3:09:25 PM
    Author     : friend
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Adicionar pessoa</title>
    </head>
    <body>
        <h1>Adicionar pessoa</h1>
        <form action="pessoa" method="post">
            CPF: <input type="text" name="cpf" value="12345678910"> <br>
            Nome: <input type="text" name="nome" value="João da Silva"> <br>
            Email: <input type="text" name="email" value="jsilva@gmail.com"> <br>
            Telefone: <input type="text" name="telefone" value="47 99223 1213"> <br>
            <input type="submit" value="Cadastrar">
        </form>
    </body>
</html>
