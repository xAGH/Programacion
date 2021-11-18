<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Editar Docente</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="../imagenes/icono.jpg" type="image/png"> 
        <link rel="stylesheet" href="../css/style.css" type="text/css">
    </head>
    <body>

<?php
   
    include '../conexion.php';


    if(isset($_GET['codprofe'])){   
    $id = $_GET['codprofe'];

    $sql_update_read = "SELECT * FROM profesor WHERE codprofe = $id";
    $result_update = mysqli_query($enlace, $sql_update_read);

    if(mysqli_num_rows($result_update) == 1){
        $row = mysqli_fetch_array($result_update);
    }}

    //Segunda consulta_Actualizar

?>

<form action="editardoc.php?codprofe=<?= $row['codprofe'] ?>" method="POST">
    <label for="codi">Código del docente*</label>       
     <br>  
   <input type="number" required value="<?= $row['codprofe'] ?>" name="cod" id="codi">
      
    <br><br>

    <label for="tipodoc">Tipo de documento*:</label>
    <select name="doc"  id="tipodoc">
    <option value="Cedula">Cédula</option>
    <option value="Pasaporte">Pasaporte</option>
    <option value="Visa">Visa</option>
    </select>
    
    <br><br>

    <label for="num">Número de documento*</label>
    <br>
    <input type="text" required name="nume" id="num" value="<?= $row['numdocprofe'] ?>">

    <br><br>

    <label for="primapell">Primer apellido*</label>
    <br>
    <input type="text" required value="<?= $row['primapellprofe'] ?>" name="prim" id="primapell">
                    
    <br><br>

    <label for="segapell">Segundo apellido*</label>
    <br>
    <input type="text" required value="<?= $row['segapellprofe'] ?>" name="seg" id="segapell">

    <br><br>

    <label for="nombre">Primer nombre*</label>
    <br>
    <input type="text" required value="<?= $row['primnomprofe'] ?>" name="nom" id="nombre">

    <br><br>

    <label for="nombre2">Segundo nombre</label>
    <br>
    <input type="text" value="<?= $row['segnomprofe'] ?>" name="nom2" id="nombre2">

    <br><br>

    <label for="email">E-mail*</label>
    <br>
    <input type="email" required value="<?= $row['emailprofe'] ?>" name="email" id="email">

    <br><br>
                    
    <label for="asig">Asignatura otorgada*</label>
    <br>
    <input type="text" required value="<?= $row['asignaturaprofe'] ?>" name="asig" id="asig">

    <br><br>

    <label for="sexo">Genero*</label>
    <select name="genero"  id="sexo">
        <option value="Masculino">Masculino</option>
        <option value="Femenino">Femenino</option>
        <option value="Prefiero no decirlo">Prefiero no decirlo</option>
        <option value="Otro">Otro</option>
    </select>

    <br><br>

    <label for="sede">Sede asignada*</label>
    <br>
    <input type="text" required value="<?= $row['sedeprofe'] ?>" name="sede" id="sede">
                    
    <br><br>

    <label for="celular">Número de teléfono*</label>
    <br>
    <input type="text" required value="<?= $row['celprofe'] ?>" name="cel" id="celular">

    <br><br>

    <p class='penviar'><input class='enviar' type="submit" name="editar" value="Actualizar Docente"></p>
    <p class="pvolver"><a href="../docente.php" class="volver">Volver</a></p>
</form>
    
<?php
    if(isset($_POST['editar'])){

        $cod = $_POST['cod'];
        $tipo = $_POST['doc'];
        $doc = $_POST['nume'];
        $apellido = $_POST['prim'];
        $apellido2 = $_POST['seg'];
        $nombre = $_POST['nom'];
        $nombre2 = $_POST['nom2'];
        $email = $_POST['email'];
        $asignatura = $_POST['asig'];
        $genero = $_POST['genero'];
        $sede = $_POST['sede'];
        $cel = $_POST['cel'];
        $id = $_GET['codprofe'];

        $sql_update = "UPDATE profesor SET tipodocprofe = '$tipo', numdocprofe = '$doc', primapellprofe = '$apellido',
        segapellprofe = '$apellido2', primnomprofe = '$nombre', segnomprofe = '$nombre2', emailprofe = '$email',
        asignaturaprofe = '$asignatura', generoprofe = '$genero', sedeprofe = '$sede', celprofe = '$cel', codprofe ='$cod' WHERE codprofe = $id";
        $result_update = mysqli_query($enlace, $sql_update);

        if($result_update){
            echo "<script>alert('Datos Actualizados Correctamente')</script>";
            echo "<script>window.location.replace('../docente.php')</script>";
        }
    }
?>
</body>
</html>