<?php
// Start the session
session_start();
?>
<?php
$_SESSION["favcolor"] = "green";
$_SESSION["favanimal"] = "cat";
echo "Variáveis de sessão armazenadas.";
?>

<a href="http://127.0.0.1:8000/03-recuperar.php">clique aqui</a> para recuperar
