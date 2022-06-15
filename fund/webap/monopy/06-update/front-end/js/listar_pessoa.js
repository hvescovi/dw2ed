$(function () { // quando o documento estiver pronto/carregado

    // código para mapear link de editar pessoa
    $(document).on("click", ".link_editar_pessoa", function () {
        eu = $(this).attr('id'); // obter id do elemento clicado
        id_pessoa = eu.split('_')[2] // editar_pessoa_N => obter id da pessoa
        // guardar o id na sessão
        sessionStorage.setItem('id_pessoa', id_pessoa);
        // encaminhar para a página de edição da pessoa
        window.location = "form_atualizar_pessoa.html";
    });

    // função para listar pessoas, a ser executada na abertura da página
    function listar_pessoas() {
        $.ajax({ // chamada ao backend
            url: 'http://localhost:5000/listar/Pessoa',
            method: 'GET',
            dataType: 'json', // dados são recebidos no formato json
            success: listar, // 
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        // função executada quando tudo dá certo
        function listar(pessoas) {
            $('#corpoTabelaPessoas').empty(); //limpar tabela

            // percorrer a lista de pessoas retornadas; 
            for (var i in pessoas) { //i vale a posição no vetor
                var lin = `<tr>
                    <td>${pessoas[i].nome}</td>
                    <td>${pessoas[i].email}</td>
                    <td>${pessoas[i].telefone}</td>
                    <td><a href=# id="editar_pessoa_${pessoas[i].id}" 
                           class="link_editar_pessoa">editar</a>
                    </tr>`;
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaPessoas').append(lin);
            }
        }
    }
    
    // código executado ao abrir a página
    listar_pessoas();

});