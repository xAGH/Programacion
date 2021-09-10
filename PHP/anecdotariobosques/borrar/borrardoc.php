<?php

    include '../conexion.php';

    if(isset($_GET['codprofe'])){

        $id=$_GET['codprofe'];


    $sql_delete = "DELETE FROM profesor WHERE codprofe=$id";

    $resultado = mysqli_query($enlace, $sql_delete);

    if($resultado){
        echo"<script>alert('Datos eliminados')</script>";
        echo"<script>window.location.replace('../docente.php')</script>";
    }
}
?>
