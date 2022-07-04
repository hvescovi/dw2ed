$(function () { // quando o documento estiver pronto/carregado

    var url = document.URL;  // exemplo: http://localhost/principal.html
    var protocolo = "http://"; // string com tamanho que desejo considerar
    var http = protocolo.length; // valor esperado: 7 (tamanho da string "http://")
    var comeco = url.substring(http); // valor esperado: localhost/principal.html
    var partes = comeco.split("/"); // quebra a string por barras; no exemplo: ['localhost','principal.html']
    var primeiro = partes[0]; // pega o que tem antes da primeira barra; variável GLOBAL

    posicao_doispontos = primeiro.indexOf(":");
    if (posicao_doispontos >= 0) { // contém dois pontos?
        meuip = primeiro.substring(0, posicao_doispontos);
    } else {
        meuip = primeiro;
    }
    var mensagem = "URL = " + url + "<br/>Endereço do servidor: "+meuip;
    $("#mostrar").html(mensagem);

    sessionStorage.setItem("meuip",meuip); // guarda na sessão

    // DESCOMENTAR A LINHA ABAIXO PARA 
    // fazer o encaminhamento automático ao início do sistema
    //window.location = "principal.html"; // vai para a página principal do sistema
});