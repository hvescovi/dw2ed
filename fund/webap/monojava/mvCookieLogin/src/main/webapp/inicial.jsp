<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>mvCookieLogin - exemplo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    </head>
    <body>
        <h1>Sistema mvCookieLogin</h1>
        <jsp:include page="subpaginaLogin.jsp"/>

        <h3>Sistema de exemplo de controle de sessão, login e cookies.</h3>

        <% if (session.getAttribute("login") != null) { // tem alguém logado?
        %>

        Menu de opções disponível apenas para usuários logados:
        <ul>
            <li>
                <a href="Geral?op=cadastroPessoas">Cadastro de pessoas</a>
            </li>
        </ul>
        <%  
            }
        %>

        <jsp:include page="subpaginaMensagem.jsp"/>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
    </body>
</html>
