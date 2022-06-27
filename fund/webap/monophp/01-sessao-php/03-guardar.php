<?php
// Start the session
session_start();
?>
<?php
valor = $_GET["chave"];
// Set session variables
$_SESSION["valor"] = valor;
echo "valor guardar: "+valor;
?>