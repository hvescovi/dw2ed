<%@page contentType="text/html" pageEncoding="UTF-8"
        import="jakarta.servlet.http.HttpSession"
        %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <!-- inclusão estática de arquivo -->
        <%@include file="menu.html" %>
        
        Bem vindo, esta é a página inicial do sistema.
        
        <!-- inclusão dinâmica de arquivo -->
        <jsp:include page="subpaginaCookies.jsp"/>
    </body>
</html>
