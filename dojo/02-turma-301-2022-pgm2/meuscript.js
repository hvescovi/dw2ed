$(function(){
    $.ajax({
        url: "http://localhost:5000/listar_carros",
        method : "GET", 
        dataType: "json",
        success: listar, 
        error: function(){
            alert("erro")
        }
    })

    function listar(carros) {
        for (var i in carros) {
            lin = '<tr>' +
            '<td>' + carros[i].ano + '</td>' +
            '<td>' + carros[i].marca + '</td>' + 
            '<td>' + carros[i].cor + '</td>' +
            '</tr>'; 
            $('#corpoTabela').append(lin);
        }
    }
});