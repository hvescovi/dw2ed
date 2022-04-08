<%-- 
    Document   : form
    Created on : Mar 17, 2022, 3:09:25 PM
    Author     : friend
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"
        import="modelo.Pessoa" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Editar pessoa</title>
    </head>
    <body>
        <h1>Editar pessoa</h1>
        <%
        Pessoa i = (Pessoa) request.getAttribute("alguem");
        %>

        <form action="pessoa?op=put" method="post">
            CPF: <input type="text" name="cpf" value="<%= i.getCpf() %>" readonly> <br>
            Nome: <input type="text" name="nome" value="<%= i.getNome() %>"> <br>
            Email: <input type="text" name="email" value="<%= i.getEmail() %>"> <br>
            Telefone: <input type="text" name="telefone" value="<%= i.getTelefone() %>"> <br>
            <input type="submit" value="Atualizar">
        </form>
    </body>
</html>
