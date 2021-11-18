<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Editar Estudiante</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="../imagenes/icono.jpg" type="image/png"> 
        <link rel="stylesheet" href="../css/style.css" type="text/css">
    </head>
    <body>

<?php
   
    include '../conexion.php';


    if(isset($_GET['idestud'])){   
    $id = $_GET['idestud'];

    $sql_update_read = "SELECT * FROM estudiante WHERE idestud = $id";
    $result_update = mysqli_query($enlace, $sql_update_read);

    if(mysqli_num_rows($result_update) == 1){
        $row = mysqli_fetch_array($result_update);
    }}

    //Segunda consulta_Actualizar

?>

<form action="editarest.php?idestud=<?= $row['idestud'] ?>" method="POST">
        <label for="cod">Código del estudiante*</label>
                <br>
                <input type="number" required value="<?= $row['codestud'] ?>" name="codestud" id="cod">

                <br><br>

                <label for="tipodoc">Tipo de documento*</label>
                <select name="tipodocumento"  id="tipodoc">
                    <option value="Tarjeta de identidad">Tarjeta de identidad</option>
                    <option value="Cedula">Cédula</option>
                    <option value="Pasaporte">Pasaporte</option>
                    <option value="Registro civil">Registro civil</option>
                </select>

                <br><br>

                <label for="numdoc">Número de documento*</label>
                <br>
                <input type="text" required value="<?= $row['numdocestud'] ?>" name="numdocestud" id="numdoc">

                <br><br>

                <label for="grado">Grado del estudiante</label>
                <br>
                <input type="text" required value="<?= $row['gradoestud'] ?>" name="gradoestud" id="grado">
                
                <br><br>

                <label for="sexo">Genero del estudiante*</label>
                <select name="genero"  id="sexo">
                    <option value="Masculino">Masculino</option>
                    <option value="Femenino">Femenino</option>
                    <option value="Prefiero no decirlo">Prefiero no decirlo</option>
                    <option value="Otro">Otro</option>
                </select>

                <br><br>

                <label for="primnom">Primer nombre*</label>
                <br>
                <input type="text" required value="<?= $row['primnomestud'] ?>" name="primnomestud" id="primnom">

                <br><br>

                <label for="segnom">Segundo nombre</label>
                <br>
                <input type="text" value="<?= $row['segnomestud'] ?>" name="segnomestud" id="segnom">

                <br><br>

                <label for="primape">Primer apellido*</label>
                <br>
                <input type="text" required value="<?= $row['primapellestud'] ?>" name="primapellestud" id="primape">

                <br><br>

                <label for="segape">Segundo apellido*</label>
                <br>
                <input type="text" required value="<?= $row['segapellestud'] ?>" name="segapellestud" id="segape">

                <br><br>

                <label for="nac">Fecha de nacimiento*</label>
                <br>
                <input class="fechanac" type="date" required value="<?= $row['fecnacestud'] ?>" name="fecnacestud" id="nac">

                <br><br>

                <label for="lugnac">Lugar de nacimiento*</label>
                <br>
                <input type="text" required value="<?= $row['lugnacestud'] ?>" name="lugnacestud" id="lugnac">

                <br><br>

                <label for="direccion">Dirección*</label>
                <br>
                <input type="text" required value="<?= $row['direcestud'] ?>" name="direcestud" id="direccion">

                <br><br>

                <label for="cel">Celular del estudiante</label>
                <br>
                <input type="text" value="<?= $row['celestud'] ?>" name="celestud" id="cel">

                <br><br>

                <label for="enfermedad">Enfermedad o discapacidad permanente</label>
                <br>
                <input type="text" value="<?= $row['enfermedad'] ?>" name="enfermedad" id="enfermedad">

                <br><br>

                <label for="medi">Medicamento permanente</label>
                <br>
                <input type="text" value="<?= $row['medipermestud'] ?>" name="medipermestud" id="medi">

                <br><br>

                <label for="tiposangre">Tipo de sangre*</label>
                <br>
                <input type="text" required value="<?= $row['tiposangre'] ?>" name="tiposangre" id="tiposangre">

                <br><br>

                <label for="eps">Eps*</label>
                <br>
                <input type="text" required value="<?= $row['tipoeps'] ?>" name="tipoeps" id="eps">

                <br><br>

                <br><br>

                <p class='penviar'><input class='enviar' type="submit" name="editar" value="Actualizar Estudiante"></p>
                <p class="pvolver"><a href="../estudiante.php" class="volver">Volver</a></p>
            </form>
    
<?php
    if(isset($_POST['editar'])){

        $cod = $_POST['codestud'];
        $numdoc = $_POST['numdocestud'];
        $primnom = $_POST['primnomestud'];
        $segnom = $_POST['segnomestud'];
        $primapell = $_POST['primapellestud'];
        $segapell = $_POST['segapellestud'];
        $fechanac = $_POST['fecnacestud'];
        $lugarnac = $_POST['lugnacestud'];
        $grado = $_POST['gradoestud'];
        $direccion = $_POST['direcestud'];
        $cel = $_POST['celestud'];
        $medic = $_POST['medipermestud'];
        $tipodoc = $_POST['tipodocumento'];
        $enfermedad = $_POST['enfermedad'];
        $genero = $_POST['genero'];
        $eps = $_POST['tipoeps'];
        $tiposangre = $_POST['tiposangre'];
        $id = $_GET['idestud'];

        $sql_update = "UPDATE estudiante SET codestud = '$cod', numdocestud = '$numdoc', primnomestud = '$primnom',
        segnomestud = '$segnom', primapellestud = '$primapell', segapellestud = '$segapell', fecnacestud = '$fechanac',
        lugnacestud = '$lugarnac', gradoestud = '$grado', direcestud = '$direccion', celestud = '$cel', medipermestud ='$medic',
        tipodocumento = '$tipodoc', enfermedad = '$enfermedad', genero ='$genero', tipoeps = '$eps', tiposangre = '$tiposangre' WHERE idestud = $id";
        $result_update = mysqli_query($enlace, $sql_update);

        if($result_update){
            echo "<script>alert('Datos Actualizados Correctamente')</script>";
            echo "<script>window.location.replace('../estudiante.php')</script>";
        }
    }
?>
</body>
</html>