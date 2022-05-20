<%@page contentType="text/html" pageEncoding="UTF-8"
        import="jakarta.servlet.http.HttpSession" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    </head>
    <body>
        <hr>
        
        <!-- objeto session implícito disponível
        goncalves2007desenvolvimento, pg 140 -->
        
        <% 
        String autorizadoExisteSTR = (String) session.getAttribute("autorizadoExiste");
        boolean autorizadoExiste = ((autorizadoExisteSTR != null) && (autorizadoExisteSTR.equals("sim")));
        
        if (autorizadoExiste) {
            
            String podeUsarCookiesSTR = (String) session.getAttribute("podeUsarCookies");
            boolean podeUsarCookies = ((podeUsarCookiesSTR != null) && (podeUsarCookiesSTR.equals("sim")));
 
            %>
            
            Já verificamos se você usa cookies => 
            <i>(podeUsarCookiesSTR <%= podeUsarCookiesSTR %>)</i> => 
        
        <%
            
            if (podeUsarCookies) {
                %>
                Fique tranquilo, estamos monitorando o uso do site via cookies ;-p
                <%
            } else {
            %>
                Você não usa cookies, mas se quiser mudar de ideia... clique aqui.
            <%
            }
        } else {
        // pergunta se o usuário aceita usar cookies
        %>
        Este site faz uso de cookies para proporcionar uma melhor experiência.
        Você aceita o uso de cookies?
        <a href="Geral?op=aceitarCookies">sim</a> | 
        <a href="Geral?op=rejeitarCookies">não</a>
        <%
        } 

        boolean analisouCookies = (Boolean) session.getAttribute("analisouCookies");
        %>
        
        <hr>
        <i>(autorizadoExisteSTR: <%= autorizadoExisteSTR %>)</i>
        <br>Sessao ID: <%= session.getId() %>
        <br>Analisou Cookies: <%= analisouCookies %>
    </body>
</html>
