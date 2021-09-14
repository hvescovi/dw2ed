
$(document).ready(function () {

    $("#geral").click(function (event) {
        // coloca na sessão o perfil 'geral'
        $.session.set('perfil', 'geral');
        // atualiza a página
        location.reload();
    });

    $("#admin").click(function (event) {
        // coloca na sessão o perfil administrador
        $.session.set('perfil', 'admin');
        // atualiza a página
        location.reload();
    });

    try {
        // tenta obter o perfil atual
        x = $.session.get('perfil');
    } catch (err) { // deu erro? Ainda não tem perfil definido? 
        // define perfil padrão: geral
        $.session.set('perfil', 'geral');
    }

    // exibe o perfil atual na tela
    $("#mensagem_perfil").val("Perfil atual: " + $.session.get('perfil'));

    // se o perfil atual for admin, exibe uma seção secreta da tela 
    if ($.session.get('perfil') == "admin") {
        $("#secreto").removeClass("d-none");
    } else {
        $("#secreto").addClass("d-none");
    }

});
