<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%@include  file="menu.html" %>

        A página DOIS tem promoções e recursos ilimitados para uso.

        <jsp:include page="subpaginaCookies.jsp"/>

        <% String visitas = (String) request.getAttribute("visitas");
        if (visitas != null) {
        %>
        <br><b>Você já visitou esta página <%= visitas %> vezes</b>
        <%
          }
        %>
    </body>
</html>
