<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Editar Anotacion</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="../imagenes/icono.jpg" type="image/png"> 
        <link rel="stylesheet" href="../css/style.css" type="text/css">
    </head>
    <body>

<?php
   
    include '../conexion.php';


    if(isset($_GET['idanotacion'])){   
    $id = $_GET['idanotacion'];

    $sql_update_read = "SELECT * FROM anotacion WHERE idanotacion = $id";
    $result_update = mysqli_query($enlace, $sql_update_read);

    if(mysqli_num_rows($result_update) == 1){
        $row = mysqli_fetch_array($result_update);
    }}

    //Segunda consulta_Actualizar

?>

<form action="editaranot.php?idanotacion=<?= $row['idanotacion'] ?>" method="POST">

<label for="cod">Código de la anotación*:</label>
    <br>
    <input type="number" required value="<?= $row['codanotacion'] ?>" name="codanot" id="cod">
  
    <br><br>

    <label for="fecha">Fecha de la anotación*</label>
    <br>
    <input type="date" required value="<?= $row['fechaanotacion'] ?>" name="fechaanot" id="fecha">
                    
    <br><br>

    <label for="des">Descripción de la anotación*</label>
    <br>
    <input type="text" required value="<?= $row['descrianotacion'] ?>" name="desc" id="des">
    
    <br><br>

    <label for="estud">Código del estudiante*</label>
                    <br>
    <input type="number" required value="<?= $row['idestud'] ?>" name="idestud" id="estud"> 

    <br><br>

    <label for="profe">Código del profesor*</label>
    <br>
    <input type="number" required value="<?= $row['codprofe'] ?>" name="codprofe" id="profe">

    <br><br>

    <label for="asignatura">Código de la asignatura*</label>
    <br>
    <input type="text" required value="<?= $row['codasignatura'] ?>" name="codasig" id="asignatura">

    <br><br>

    <label for="falta">Código de la falta*</label>
    <br>
    <input type="number" required value="<?= $row['codtipofalta'] ?>" name="codfalta" id="falta">

    <br><br>

    <p class='penviar'><input class='enviar' type="submit" name="editar" value="Actualizar Anotación"></p>
    <p class="pvolver"><a href="../anotacion.php" class="volver">Volver</a></p>
</form>
    
<?php
    if(isset($_POST['editar'])){
        $codanot = $_POST['codanot'];
        $fecha = $_POST['fechaanot'];
        $descrip = $_POST['desc'];
        $idestud = $_POST['idestud'];
        $codprofe = $_POST['codprofe'];
        $codasig = $_POST['codasig'];
        $codfalta = $_POST['codfalta'];
        $id = $_GET['idanotacion'];


        $sql_update = "UPDATE anotacion SET codanotacion = '$codanot', 	fechaanotacion = '$fecha', 	descrianotacion = '$descrip', idestud = '$idestud',
        codprofe = '$codprofe', codasignatura = '$codasig', codtipofalta = '$codfalta' WHERE idanotacion = $id";
        $result_update = mysqli_query($enlace, $sql_update);

        if($result_update){
            echo "<script>alert('Datos Actualizados Correctamente')</script>";
            echo "<script>window.location.replace('../anotacion.php')</script>";
        }
    }
?>
</body>
</html>


