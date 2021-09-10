<?php

    include '../conexion.php';

    if(isset($_GET['idestud'])){

        $id=$_GET['idestud'];


    $sql_delete = "DELETE FROM estudiante WHERE idestud=$id";

    $resultado = mysqli_query($enlace, $sql_delete);

    if($resultado){
        echo"<script>alert('Datos eliminados')</script>";
        echo"<script>window.location.replace('../estudiante.php')</script>";
    }
}
?>
