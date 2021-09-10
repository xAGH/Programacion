<?php
    $servidor="localhost";
    $usuario="root";
    $clave="";
    $bdd="anecdotariobosques1";

    $enlace = mysqli_connect($servidor, $usuario, $clave, $bdd);

    if(!$enlace){
        echo"Error en la conexión con el servidor";
    }
?>