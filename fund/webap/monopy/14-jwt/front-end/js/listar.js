$(function () { // quando o documento estiver pronto/carregado

    meuip = sessionStorage.getItem("meuip");

    // verifica se está logado
    login = sessionStorage.getItem("login");

    if (login !== null) {

        // obtém a JWT
        jwt = sessionStorage.getItem("JWT");

        $.ajax({
            url: `http://${meuip}:5000/listar/Pessoa`,
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'text/plain',
            headers: { Authorization: 'Bearer ' + jwt },
            success: listar, // chama a função listar para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        // função executada quando tudo dá certo
        function listar(retorno) {
            if (retorno.resultado == 'ok') {
                // percorrer a lista de pessoas retornadas; 
                pessoas = retorno.detalhes;
                for (var i in pessoas) { //i vale a posição no vetor
                    var lin = `<tr>
                <td>${pessoas[i].nome}</td>
                <td>${pessoas[i].email}</td>
                <td>${pessoas[i].telefone}</td>
                </tr>`;

                    // adiciona a linha no corpo da tabela
                    $('#corpoTabelaPessoas').append(lin);
                }
            } else {
                alert("Erro: " + retorno.detalhes);
            }
        }
    } else {
        alert("Você não está logado, por favor, conecte-se");
        window.location = "index.html";
    }

});