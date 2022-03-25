<%-- 
    Document   : listar.jsp
    Created on : Mar 18, 2022, 5:32:43 AM
    Author     : friend
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"
        import="java.util.*"
        import="modelo.Pessoa" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Exibir pessoa</h1>
        <%
            
        // goncalves2007, pg 420
        Pessoa i = (Pessoa) request.getAttribute("alguem");
                 
        %>

        CPF: <%= i.getCpf() %> <br> 
        Nome: <%= i.getNome() %> <br>
        Email: <%= i.getEmail() %> <br>
        Telefone: <%= i.getTelefone() %> 
        
        <a href="pessoa?d=<%= i.getCpf() %>">remover</a><br>
        

       

    </body>
</html>
