// obtém login da sessão
var login = sessionStorage.getItem('login');
alert(login);
var mensagem = "";
var logado = false;
// o login existe?
if (login === null) {
    mensagem = `Você ainda não fez login. <a href=form_login.html>Faça agora</a> :-)`;
} else {
    logado = true;
    mensagem = `Bem vindo, ${login}`;
    // carrega o menu de opções
    $("#menu").load('opcoes.html');
}
$("#mensagem").html(mensagem);