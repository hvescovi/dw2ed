$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirLivros", function () {
        var form_data = new FormData($('#meuform')[0]);

        $.ajax({
            url: 'http://localhost:5000/salvar_imagem',
            type: 'POST',
            //dataType: 'json',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
               // $("#nomearquivo").text(data.arquivo);
                //alert(data.arquivo);
                //alert(data);
                alert("enviou a foto direitinho!");
            },
            error: function(data) {
                alert("deu ruim na foto");
            }
        });
        //pegar dados da tela
        ISBN = $("#campoISBN").val();
        // C:\\fakepath\\olho.jpg"
        // só conta a contrabarra uma vez, inicia do zero
        Capa_do_livro =$("#campoCapa_do_Livro").val().substr(12); 
        Nome_do_livro = $("#campoNome_do_livro").val();
        Autor = $("#campoAutor").val();
        Paginas = $("#campoPaginas").val();
        Editora = $("#campoEditora").val();
        Status = $("#campoStatus").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ ISBN: ISBN, Capa_do_livro: Capa_do_livro, Nome_do_livro: Nome_do_livro, Autor:Autor, Paginas:Paginas, Editora:Editora, Status:Status });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_livro',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: incluir_livro, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function incluir_livro (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("livro cadastrado com sucesso!");
                // limpar os campos
                $("#campoISBN").val();
                $("#campoCapa do Livros").val();
                $("#campoNome_do_livro").val();
                $("#campoAutor").val();
                $("#campoPaginas").val();
                $("#campoEditora").val();
                $("#campoStatus").val();
            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
});

$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btCadastrar", function () {
        //pegar dados da tela
        Nome = $("#campoNome").val();
        Idade= $("#campoIdade").val();
        Email = $("#campoEmail").val();
        Senha = $("#campoSenha").val();
        Repetir_senha = $("#campoRepetir_senha").val();
        // preparar dados no formato json
        var Cadados = JSON.stringify({ Nome: Nome, Idade: Idade, Email: Email, Senha:Senha, Repetir_senha:Repetir_senha });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/cadastrar_usuario',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: Cadados, // estes são os dados enviados
            success: cadastrar_usuario, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function cadastrar_usuario (retorno_cad) {
            if (retorno_cad.resultado_cad == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("livro cadastrado com sucesso!");
                // limpar os campos
                $("#campoNome").val();
                $("#campoIdade").val();
                $("#campoEmail").val();
                $("#campoSenha").val();
                $("#campoRepetir_senha").val();
            } else {
                // informar mensagem de erro
                alert(retorno_cad.resultado_cad + ":" + retorno_cad.detalhes);
            }            
        }
        function erroAoIncluir (retorno_cad) {
            // informar mensagem de erro
            alert("ERRO: "+retorno_cad.resultado_cad + ":" + retorno_cad.detalhes);
        }
    });
});
$(function () { // quando o documento estiver pronto/carregado
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btLogin", function () {
        //pegar dados da tela
        Email = $("#campoEmail").val();
        Senha = $("#campoSenha").val();
        // preparar dados no formato json
        var Cadados = JSON.stringify({Email: Email, Senha:Senha});
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/login_usuario',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: Cadados, // estes são os dados enviados
            success: cadastrar_usuario, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function cadastrar_usuario (resposta) {
            if (resposta.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("login feito");
                // limpar os campos
                $("#campoEmail").val();
                $("#campoSenha").val();
            } else {
                // informar mensagem de erro
                alert("erssro");
            }            
        }
        function erroAoIncluir (resposta) {
            // informar mensagem de erro
            alert("ERRO:"+ resposta.detalhes);
        }
    });
});