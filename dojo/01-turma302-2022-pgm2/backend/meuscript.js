$(function() {
    $.ajax({
        url: 'http://localhost:5000/listar_carros',
        method:'GET',
        dataType: 'json', 
        success: listar,
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });
})