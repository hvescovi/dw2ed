<%-- 
    Document   : result
    Created on : Mar 29, 2022, 3:43:15 PM
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
        
        <%= request.getAttribute("message") %>
        
        <a href="index.html">Retornar</a>
    </body>
</html>
