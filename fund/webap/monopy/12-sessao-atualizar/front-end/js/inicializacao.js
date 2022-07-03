$(function () { // quando o documento estiver pronto/carregado

    var url = document.URL;  // exemplo: http://localhost/principal.html
    var protocolo = "http://"; // string com tamanho que desejo considerar
    var http = protocolo.length; // valor esperado: 7 (tamanho da string "http://")
    var comeco = url.substring(http); // valor esperado: localhost/principal.html
    var partes = comeco.split("/"); // quebra a string por barras; no exemplo: ['localhost','principal.html']
    meuip = partes[0]; // pega o que tem antes da primeira barra; variável GLOBAL

    sessionStorage.setItem("meuip",meuip); // guarda na sessão

    window.location = "principal.html"; // vai para a página principal do sistema
});