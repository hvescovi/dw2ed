$(function () { // quando o documento estiver pronto/carregado

    meuip = sessionStorage.getItem("meuip");

    login = sessionStorage.getItem("login");
    var dados = JSON.stringify({ login: login });        

    $.ajax({
        url: `http://${meuip}:5000/listar/Pessoa`, // uso de template string
        method: 'POST',
        dataType: 'json', // os dados são recebidos no formato json
        contentType: 'application/json', // tipo dos dados enviados
        data: dados, // estes são os dados enviados
        xhrFields: { withCredentials: true },
        crossDomain: true,
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

    // código para mapear link de editar pessoa
    $(document).on("click", ".link_editar_pessoa", function () {
        eu = $(this).attr('id'); // obter id do elemento clicado
        id_pessoa = eu.split('_')[2] // editar_pessoa_N => obter id da pessoa
        sessionStorage.setItem('id_pessoa', id_pessoa); // guardar o id na sessão
        // encaminhar para a página de edição da pessoa
        window.location = "form_atualizar_pessoa.html";
    });

});