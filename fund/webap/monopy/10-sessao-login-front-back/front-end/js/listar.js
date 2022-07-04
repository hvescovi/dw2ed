$(function () { // quando o documento estiver pronto/carregado

    meuip = sessionStorage.getItem("meuip");

    //alert(meuip);
    $.ajax({
        url: `http://${meuip}:5000/listar/Pessoa`, // uso de template string
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    // função executada quando tudo dá certo
    function listar(resultado) {
        // percorrer a lista de pessoas retornadas; 
        pessoas = resultado;
        for (var i in pessoas) { //i vale a posição no vetor
            var lin = `<tr>
                <td>${pessoas[i].nome}</td>
                <td>${pessoas[i].email}</td>
                <td>${pessoas[i].telefone}</td>
                </tr>`;

            // adiciona a linha no corpo da tabela
            $('#corpoTabelaPessoas').append(lin);
        }
    }

});