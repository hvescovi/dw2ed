<?php
// Start the session
session_start();
?>

<?php
$chave = $_GET["chave"];
$valor = $_GET["valor"];
$_SESSION[$chave] = $valor;
echo "valor guardado! ";
?>