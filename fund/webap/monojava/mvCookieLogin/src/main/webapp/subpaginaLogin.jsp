<%@page contentType="text/html" pageEncoding="UTF-8"
        import="jakarta.servlet.http.HttpSession" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        
        <%
            // verificar se foi feito login
            String login = (String) session.getAttribute("login");
            if (login != null) {
        %>
        Bem vindo, <%= login %>. <a href="Geral?op=logout">(logout)</a>
        <%
            } else { %>
            Você precisa <a href="Geral?op=formlogin">fazer login</a> no sistema.
        <%
            }
        %>
    </body>
</html>
