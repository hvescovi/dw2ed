$(function () { // quando o documento estiver pronto/carregado

    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btLogin", function () {
        //pegar dados da tela
        login = $("#campoLogin").val();
        senha = $("#campoSenha").val();
        
        if (login == "mylogin" && senha == "123") {
            // guarda na sessao
            sessionStorage.setItem('login', login);

            // encaminha para a página principal
            window.location = 'principal.html';
        } else {
            alert("Login ou senha inválido(s)!!");
        }        
    });   

});