<?php

    include '../conexion.php';

    if(isset($_GET['idanotacion'])){

        $id=$_GET['idanotacion'];


    $sql_delete = "DELETE FROM anotacion WHERE idanotacion=$id";

    $resultado = mysqli_query($enlace, $sql_delete);

    if($resultado){
        echo"<script>alert('Datos eliminados')</script>";
        echo"<script>window.location.replace('../anotacion.php')</script>";
    }
}
?>
