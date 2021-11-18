<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Editar Tipo de Sangre</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="../imagenes/icono.jpg" type="image/png"> 
        <link rel="stylesheet" href="../css/style.css" type="text/css">
    </head>
    <body>

<?php
   
    include '../conexion.php';


    if(isset($_GET['idtiposangre'])){   
    $id = $_GET['idtiposangre'];

    $sql_update_read = "SELECT * FROM tiposangre WHERE idtiposangre = $id";
    $result_update = mysqli_query($enlace, $sql_update_read);

    if(mysqli_num_rows($result_update) == 1){
        $row = mysqli_fetch_array($result_update);
    }}

    //Segunda consulta_Actualizar

?>

    <form action="editarsan.php?idtiposangre=<?= $row['idtiposangre'] ?>"  method="POST">
        <label for="nombre">Nombre del tipo de sangre*</label>

        <br>

        <input type="text" required name="nombresan" id="nombre" value="<?= $row['nomtiposangre'] ?>">

        <br>

        <p class='penviar'><input class='enviar' type="submit" name="editar" value="Actualizar: '<?=$row['nomtiposangre']?>'"></p>
        <p class="pvolver"><a href="../tiposangre.php" class="volver">Volver</a></p>
    </form>
<?php
    if(isset($_POST['editar'])){
        $nombre = $_POST['nombresan'];
        $id = $_GET['idtiposangre'];

        $sql_update = "UPDATE tiposangre SET nomtiposangre = '$nombre' WHERE idtiposangre = $id";
        $result_update = mysqli_query($enlace, $sql_update);

        if($result_update){
            echo "<script>alert('Datos Actualizados Correctamente')</script>";
            echo "<script>window.location.replace('../tiposangre.php')</script>";
        }
    }
?>
</body>
</html>