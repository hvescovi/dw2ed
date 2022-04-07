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
        <h1>Listagem de pessoas</h1>
        <%
            
        // goncalves2007, pg 420
        ArrayList<Pessoa> registros = (ArrayList<Pessoa>) request.getAttribute("registros");
                 
        for (Pessoa i : registros) {
        
        %>

        <%= i.getCpf() %>, <%= i.getNome() %>, 
        <%= i.getEmail() %>, <%= i.getTelefone() %> 
        
        | <a href="pessoa?op=d&q=<%= i.getCpf() %>">remover</a> | 
        <a href="pessoa?op=r&q=<%= i.getCpf() %>">exibir</a> | 
        <a href="pessoa?op=a&q=<%= i.getCpf() %>">atualizar</a> <br>

        <%
            }
        %>

        Fim da listagem

    </body>
</html>
