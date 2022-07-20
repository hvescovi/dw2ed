$(function () {

    
    // obtém login da sessão
    var login = sessionStorage.getItem('login');
    var mensagem = "";
    // o login existe?
    if (login === null) {
        mensagem = `Você ainda não fez login. <a href=form_login.html>Faça agora</a> :-)`;
    } else {
        mensagem = `Bem vindo, ${login}.`;
        // carrega o menu de opções

        $("#menu").html(`
        
        Menu de opções:
        <a href="principal.html">Início</a> | 
        <a href="listar.html" id="linkListarPessoas">Listar</a> |
        Incluir |
        Opções |
        <a href=# id="linkLogout">Logout</a>
                
        `);
        
    }
    // exibe a mensagem na tela
    $("#mensagem").html(mensagem);

    // código para mapear click do botão de logout
    $(document).on("click", "#linkLogout", function () {
        // remove itens da sessao
        sessionStorage.removeItem('login');
        sessionStorage.removeItem('jwt');
        // atualiza a tela
        window.location = 'principal.html';
    });

});