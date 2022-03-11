<%-- 
    Document   : listar_pessoas
    Created on : Mar 11, 2022, 6:28:02 AM
    Author     : friend
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Listagem de pessoas</title>
    </head>
    <body>
        <h1>Exibindo uma pessoa</h1>
        
        <jsp:useBean id="pdao" class="dao.estatico.PessoaDAO"/>  
        
        Nome: <%= pdao.retornarPessoa("qualquer").getNome() %>       
      
    </body>
</html>
