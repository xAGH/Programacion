<?php

    include '../conexion.php';

    if(isset($_GET['ideps'])){

        $id=$_GET['ideps'];


    $sql_delete = "DELETE FROM eps WHERE ideps=$id";

    $resultado = mysqli_query($enlace, $sql_delete);

    if($resultado){
        echo"<script>alert('Datos eliminados')</script>";
        echo"<script>window.location.replace('../eps.php')</script>";
    }
}
?>
