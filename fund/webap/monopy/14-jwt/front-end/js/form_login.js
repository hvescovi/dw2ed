$(function () { // quando o documento estiver pronto/carregado

    meuip = sessionStorage.getItem("meuip");
    
    // código para mapear click do botão login
    $(document).on("click", "#btLogin", function () {
        //pegar dados da tela
        login = $("#campoLogin").val();
        senha = $("#campoSenha").val();

        // preparar dados no formato json
        var dados = JSON.stringify({ login: login, senha: senha });

        // fazer requisição para o back-end
        $.ajax({
            url: `http://${meuip}:5000/login`,
            method: 'POST', 
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'text/plain', // tipo dos dados enviados
            //contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: loginOk, // chama a função listar para processar o resultado
            error: function (xhr, status, error) {
                alert("Erro na conexão, verifique o backend. " + xhr.responseText + " - " + status + " - " + error);
                // https://api.jquery.com/jquery.ajax/
            }
        });
        function loginOk(retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // guarda na sessao o login
                sessionStorage.setItem('login', login);
                // guarda na sessao da JWT
                sessionStorage.setItem('jwt', retorno.detalhes);
                // encaminha para a página principal
                window.location = 'principal.html';
            } else {
                // informar mensagem de erro
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
            }
        }

    });

});

// https://flask-jwt-extended.readthedocs.io/en/stable/token_locations/