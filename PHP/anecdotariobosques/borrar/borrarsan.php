<?php

    include '../conexion.php';

    if(isset($_GET['idtiposangre'])){

        $id=$_GET['idtiposangre'];


    $sql_delete = "DELETE FROM tiposangre WHERE idtiposangre=$id";

    $resultado = mysqli_query($enlace, $sql_delete);

    if($resultado){
        echo"<script>alert('Datos eliminados')</script>";
        echo"<script>window.location.replace('../tiposangre.php')</script>";
    }
}
?>
