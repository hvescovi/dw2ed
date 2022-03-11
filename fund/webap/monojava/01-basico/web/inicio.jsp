<%-- 
    Document   : inicio
    Created on : Mar 11, 2022, 5:05:34 AM
    Author     : friend
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"
        import="java.util.*"
        import="java.text.SimpleDateFormat"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Olá mundo!</h1>
        <%
Date hoje = new Date();
SimpleDateFormat formato = new SimpleDateFormat("dd/MM/yy");
        %>
        Hoje é: <% out.print(formato.format(hoje)); %>
    </body>
</html>
