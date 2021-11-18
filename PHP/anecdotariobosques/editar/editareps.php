<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Editar EPS</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="../imagenes/icono.jpg" type="image/png"> 
        <link rel="stylesheet" href="../css/style.css" type="text/css">
    </head>
    <body>

<?php
   
    include '../conexion.php';


    if(isset($_GET['ideps'])){   
    $id = $_GET['ideps'];

    $sql_update_read = "SELECT * FROM eps WHERE ideps = $id";
    $result_update = mysqli_query($enlace, $sql_update_read);

    if(mysqli_num_rows($result_update) == 1){
        $row = mysqli_fetch_array($result_update);
    }}

    //Segunda consulta_Actualizar

?>

    <form action="editareps.php?ideps=<?= $row['ideps'] ?>"  method="POST">
    <label for="nombre">Nombre de la Eps*</label>
        <br>
        <input type="text" required name="nombreeps" id="nombre" value="<?= $row['nombreeps'] ?>">

        <p class='penviar'><input class='enviar' type="submit" name="editar" value="Actualizar Eps"></p>

        <p class="pvolver"><a href="../eps.php" class="volver">Volver</a></p>

    </form>
<?php
    if(isset($_POST['editar'])){
        $nombre = $_POST['nombreeps'];
        $id = $_GET['ideps'];

        $sql_update = "UPDATE eps SET nombreeps = '$nombre' WHERE ideps = $id";
        $result_update = mysqli_query($enlace, $sql_update);

        if($result_update){
            echo "<script>alert('Datos Actualizados Correctamente')</script>";
            echo "<script>window.location.replace('../eps.php')</script>";
        }
    }
?>
</body>
</html>