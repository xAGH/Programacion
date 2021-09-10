<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Editar Asignatura</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="../imagenes/icono.jpg" type="image/png"> 
        <link rel="stylesheet" href="../css/style.css" type="text/css">
    </head>
    <body>

<?php
   
    include '../conexion.php';


    if(isset($_GET['idasignatura'])){   
    $id = $_GET['idasignatura'];

    $sql_update_read = "SELECT * FROM asignatura WHERE idasignatura = $id";
    $result_update = mysqli_query($enlace, $sql_update_read);

    if(mysqli_num_rows($result_update) == 1){
        $row = mysqli_fetch_array($result_update);
    }}

    //Segunda consulta_Actualizar

?>

    <form action="editarasig.php?idasignatura=<?= $row['idasignatura'] ?>"  method="POST">

        <label for="nombre">Nombre de la Asignatura*</label>
        <br>
        <input type="text" required name="asignatura" id="nombre" value="<?= $row['nomasignatura'] ?>">

        <p class='penviar'><input class='enviar' type="submit" name="editar" value="Actualizar Asignatura"></p>

        <p class="pvolver"><a href="../asignatura.php" class="volver">Volver</a></p>

    </form>
<?php
    if(isset($_POST['editar'])){
        $nombre = $_POST['asignatura'];
        $id = $_GET['idasignatura'];

        $sql_update = "UPDATE asignatura SET nomasignatura = '$nombre' WHERE idasignatura = $id";
        $result_update = mysqli_query($enlace, $sql_update);

        if($result_update){
            echo "<script>alert('Datos Actualizados Correctamente')</script>";
            echo "<script>window.location.replace('../asignatura.php')</script>";
        }
    }
?>