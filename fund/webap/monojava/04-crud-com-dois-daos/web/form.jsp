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
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <form action="pessoa" method="post">
            Nome: <input type="text" name="nome" value="João da Silva"> <br>
            Email: <input type="text" name="email" value="jsilva@gmail.com"> <br>
            Telefone: <input type="text" name="telefone" value="47 99223 1213"> <br>
            <input type="submit" value="Cadastrar">
        </form>
    </body>
</html>
