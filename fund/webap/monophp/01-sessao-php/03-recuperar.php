<?php
// Start the session
session_start();
?>
<?php
echo $_SESSION["favcolor"];
echo $_SESSION["favanimal"];
echo "Variáveis de sessão recuperadas";
?>