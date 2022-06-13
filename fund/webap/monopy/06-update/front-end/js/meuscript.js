$(function () { // quando o documento estiver pronto/carregado

    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btAtualizarPessoa", function () {
        //pegar dados da tela
        id = $("#campoId").val();
        nome = $("#campoNome").val();
        email = $("#campoEmail").val();
        tel = $("#campoTelefone").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, email: email, telefone: tel });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/atualizar/Pessoa',
            type: 'PUT',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: pessoaAtualizada, // chama a função listar para processar o resultado
            error: erroAoAtualizar
        });
        function pessoaAtualizada(retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Pessoa atualizada com sucesso!");
            } else {
                // informar mensagem de erro
                alert("ERRO na atualização: " + retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoAtualizar(retorno) {
            // informar mensagem de erro
            alert("ERRO ao contactar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });

    // código para mapear click do botão incluir pessoa
    $(document).on("click", ".link_editar_pessoa", function () {

        eu = $(this).attr('id');
        id_pessoa = eu.split('_')[2] // editar_pessoa_N
        alert(id_pessoa);

        // guarda o id na sessão
        sessionStorage.setItem('id_pessoa', id_pessoa);

        // encaminha para a página de edição da pessoa
        windows.location = "form_atualizar.html"
    });

    function inicializacao_form_editar_pessoa() {

        // restaura o id de quem está sendo editado
        var id_pessoa = sessionStorage.getItem('id_pessoa');

        // chamada ao backend
        $.ajax({
            url: 'http://localhost:5000/retornar/Pessoa/'+id_pessoa,
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: exibir_no_form, // chama a função listar para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        // função executada quando tudo dá certo
        function exibir_no_form(retorno) {
            if (retorno.resultado == "ok") {
                pessoa = retorno.detalhes;
                $("$campoNome").val(pessoa.nome);
                $("$campoEmail").val(pessoa.email);
                $("$campoTelefone").val(pessoa.telefone);
            } else {
                alert("ERRO: "+retorno.detalhes)
            }
        } 
    }

    function listar_pessoas() {

        // chamada ao backend
        $.ajax({
            url: 'http://localhost:5000/listar/Pessoa',
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: listar, // chama a função listar para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });

        // função executada quando tudo dá certo
        function listar(pessoas) {
            // percorrer a lista de pessoas retornadas; 
            for (var i in pessoas) { //i vale a posição no vetor
                lin = ```<tr>
                    <td>' + pessoas[i].nome + </td>
                    <td>' + pessoas[i].email + </td>
                    <td>' + pessoas[i].telefone + </td>
                    <td><a href=# id="editar_pessoa_${pessoas[i].id}" 
                           class="link_editar_pessoa">editar</a>
                    </tr>```
                // adiciona a linha no corpo da tabela
                $('#corpoTabelaPessoas').append(lin);
            }
        }
    } 

});