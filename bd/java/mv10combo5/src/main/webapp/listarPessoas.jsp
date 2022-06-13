<%@page contentType="text/html" pageEncoding="UTF-8"
        import="java.util.*"
        import="ifc.edu.br.mv10combo5.model.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <h1>Listagem de Pessoas</h1>
        <%
        ArrayList<Pessoa> pessoas = (ArrayList<Pessoa>) request.getAttribute("pessoas");
        %>

        <%
        for (Pessoa pessoa : pessoas) {
        %>
        <%=pessoa.getId()%>, <%=pessoa.getNome()%>
        <%
          }
        %>
    </body>
</html>
