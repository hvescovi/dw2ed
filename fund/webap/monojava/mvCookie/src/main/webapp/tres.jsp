<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%@include  file="menu.html" %>
        
        Talvez esta seja a MELHOR página do sistema! A página TRÊS.
        
        <jsp:include page="subpaginaCookies.jsp"/>
    </body>
</html>
