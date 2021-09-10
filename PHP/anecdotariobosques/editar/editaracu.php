<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Editar Acudiente</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="../imagenes/icono.jpg" type="image/png"> 
        <link rel="stylesheet" href="../css/style.css" type="text/css">
    </head>
    <body>

<?php
   
    include '../conexion.php';


    if(isset($_GET['numero_documento'])){   
    $id = $_GET['numero_documento'];

    $sql_update_read = "SELECT * FROM acudiente WHERE numero_documento = $id";
    $result_update = mysqli_query($enlace, $sql_update_read);

    if(mysqli_num_rows($result_update) == 1){
        $row = mysqli_fetch_array($result_update);
    }}

    //Segunda consulta_Actualizar

?>

<form action="editaracu.php?numero_documento=<?= $row['numero_documento'] ?>" method="POST">

    <label for="codigo">Número de documento del acudiente*</label>       
    <br>  
    <input type="number" required value="<?= $row['numero_documento'] ?>" name="doc" id="codigo">

    <br><br>

    <label for="nombre">Nombre del acudiente*</label>
    <br>
    <input type="text" required value="<?= $row['nomacudiente'] ?>" name="nom" id="nombre">

    <br><br>

    <label for="direccion">Dirección del acudiente*</label>
    <br>
    <input type="text" required value="<?= $row['diracudiente'] ?>" name="direc" id="direccion">

    <br><br>

    <label for="telefono">Número telefónico*</label>
    <br>
    <input type="text" required value="<?= $row['telacudiente'] ?>" name="tele" id="telefono">

    <br><br>

    <label for="correo">Correo*</label>
    <br>
    <input type="email" required value="<?= $row['correoacudiente'] ?>" name="email" id="correo">

    <br><br>

    <label for="sexo">Genero*</label>
    <select name="genero"  id="sexo">
        <option value="Masculino">Masculino</option>
        <option value="Femenino">Femenino</option>
        <option value="Prefiero no decirlo">Prefiero no decirlo</option>
        <option value="Otro">Otro</option>
    </select>

    <br><br>

    <p class='penviar'><input class='enviar' type="submit" name="editar" value="Actualizar Acudiente"></p>
    <p class="pvolver"><a href="../acudiente.php" class="volver">Volver</a></p>
</form>
    
<?php
    if(isset($_POST['editar'])){
        $id= $_GET['numero_documento'];
        $doc = $_POST['doc'];
        $nombre = $_POST['nom'];
        $direc = $_POST['direc'];
        $tele = $_POST['tele'];
        $email = $_POST['email'];
        $genero = $_POST['genero'];


        $sql_update = "UPDATE acudiente SET numero_documento = '$doc', nomacudiente = '$nombre', diracudiente = '$direc', telacudiente = '$tele',
        correoacudiente = '$email', genero = '$genero' WHERE numero_documento = $id";
        $result_update = mysqli_query($enlace, $sql_update);

        if($result_update){
            echo "<script>alert('Datos Actualizados Correctamente')</script>";
            echo "<script>window.location.replace('../acudiente.php')</script>";
        }
    }
?>
</body>
</html>


