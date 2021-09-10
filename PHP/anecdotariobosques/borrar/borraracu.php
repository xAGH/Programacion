<?php

    include '../conexion.php';

    if(isset($_GET['numero_documento'])){

        $id=$_GET['numero_documento'];


    $sql_delete = "DELETE FROM acudiente WHERE numero_documento=$id";

    $resultado = mysqli_query($enlace, $sql_delete);

    if($resultado){
        echo"<script>alert('Datos eliminados')</script>";
        echo"<script>window.location.replace('../acudiente.php')</script>";
    }
}
?>
