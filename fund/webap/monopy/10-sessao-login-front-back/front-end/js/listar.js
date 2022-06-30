$(function () { // quando o documento estiver pronto/carregado

        $.ajax({
            url: 'http://localhost:5000/listar/Pessoa',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar, // chama a função listar para processar o resultado
            xhrFields: {
                withCredentials: true
            },
            crossDomain: true,
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        // função executada quando tudo dá certo
        function listar(pessoas) {
            // percorrer a lista de pessoas retornadas; 
            for (var i in pessoas) { //i vale a posição no vetor
                lin = '<tr>' + // elabora linha com os dados da pessoa
                    '<td>' + pessoas[i].nome + '</td>' +
                    '<td>' + pessoas[i].email + '</td>' +
                    '<td>' + pessoas[i].telefone + '</td>' +
                    '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaPessoas').append(lin);
            }
        }

    });