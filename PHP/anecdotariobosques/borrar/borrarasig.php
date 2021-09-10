<?php

    include '../conexion.php';

    if(isset($_GET['idasignatura'])){

        $id=$_GET['idasignatura'];


    $sql_delete = "DELETE FROM asignatura WHERE idasignatura=$id";

    $resultado = mysqli_query($enlace, $sql_delete);

    if($resultado){
        echo"<script>alert('Datos eliminados')</script>";
        echo"<script>window.location.replace('../asignatura.php')</script>";
    }
}
?>
