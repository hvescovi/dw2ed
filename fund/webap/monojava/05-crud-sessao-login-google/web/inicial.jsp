<%@page contentType="text/html" pageEncoding="UTF-8"
        import="jakarta.servlet.http.HttpSession"
        %>
<!DOCTYPE html>
<html>
    <head>
        <title>Cadastro de pessoas</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>

        
        <h1>Cadastro de pessoas</h1>

        <div id="email"></div>

        <div id="email-sessao"></div>


        <% 
        String login = (String) session.getAttribute("login");
        if (login != null) {
        %>
        Sessão no servidor: <%= login %>

        <a href="sessao?op=logout">Logout</a>
        <% 
            } else {
        %>
        Sessão inativa no servidor
        <% } %>



        <ul>
            <li>
                <a href="pessoa">Listar</a>
            </li>
            <li>
                <a href="pessoa?op=f">Inserir</a>
            </li>
        </ul>

        <hr>
        <div id="buttonDiv"></div> 

        
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

        <!-- login com google! -->
        <script src="https://accounts.google.com/gsi/client" async defer></script>

        <script>
            function handleCredentialResponse(response) {

                console.log("Encoded JWT ID token: " + response.credential);

                token = response.credential;

                resp = JSON.parse(atob(token.split('.')[1]));
                //console.log(JSON.stringify(resp));
                //alert(resp.email);

                $("#email").text("Bem vindo, " + resp.email);

                // informar o servidor de que o front-end está logado
                $.get("sessao?op=login&email=" + resp.email, function (data) {
                    //alert("recebido: "+data);
                    if (data === "ok") {
                        $("#email-sessao").text("Sessão ativa via JS: " + resp.email);
                        // atualizar a página
                        //document.location.reload(true);
                    } else {
                        $("#email-sessao").text("Problema na sessão: " + data);
                    }
                });



                /*
                 // decodeJwtResponse() is a custom function defined by you
                 // to decode the credential response.
                 const responsePayload = decodeJwtResponse(response.credential);
                 
                 console.log("ID: " + responsePayload.sub);
                 console.log('Full Name: ' + responsePayload.name);
                 console.log('Given Name: ' + responsePayload.given_name);;
                 console.log('Family Name: ' + responsePayload.family_name);
                 console.log("Image URL: " + responsePayload.picture);
                 console.log("Email: " + responsePayload.email);
                 
                 */
            }
            window.onload = function () {
                google.accounts.id.initialize({
                    client_id: "523415345044-d0c904843j1aj1nsu8bkfvjcim42e2fe.apps.googleusercontent.com",
                    callback: handleCredentialResponse
                });
                google.accounts.id.renderButton(
                        document.getElementById("buttonDiv"),
                        {theme: "outline", size: "large"}  // customization attributes
                );
                google.accounts.id.prompt(); // also display the One Tap dialog
            };




        </script>


    </body>
</html>
