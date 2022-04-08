<%-- 
    Document   : mensagem
    Created on : Mar 18, 2022, 5:17:07 AM
    Author     : friend
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Mensagem</title>
    </head>
    <body>
        <h1>Mensagem</h1>
        
        <h3> <%= (String) request.getAttribute("msg") %> </h3>
        
        <a href="geral">Retornar ao início</a>
        
    </body>
</html>
