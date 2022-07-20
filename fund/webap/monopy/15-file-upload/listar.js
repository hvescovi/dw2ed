$(function () {

    $(document).on("click", "#btListar", function () {

        // chamada ao backend
        $.ajax({
            url: 'http://localhost:5000/retornar_pessoas',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar_pessoas, // chama a função listar para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        // função executada quando tudo dá certo
        function listar_pessoas(retorno) {
            if (retorno.resultado == 'ok') {
                pessoas = retorno.detalhes;
                // percorrer a lista de pessoas retornadas; 
                for (var i in pessoas) { //i vale a posição no vetor
                    lin = '<tr>' + // elabora linha com os dados da pessoa
                        '<td>' + pessoas[i].nome + '</td>' +
                        '<td>' + pessoas[i].email + '</td>' +
                        '<td><img src="http://localhost:5000/get_image/' + pessoas[i].id + '"></td>' +
                        '</tr>';
                    // adiciona a linha no corpo da tabela
                    $('#corpoTabelaPessoas').append(lin);
                }
            } else {
                alert("erro no retorno: " + retorno.detalhes);
            }
        }

    });
});