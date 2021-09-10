<?php
    include ("conexion.php");
?>
<!DOCTYPE html> 
<html>
    <head>
        <link rel="shortcut icon" href="Imagenes/icono.jpg" type="image/png">
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Estudiante</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="css/style.css" type="text/css">
    </head>
    <script type="text/javascript">
        function ConfirmDelete(){
            var respuesta = confirm("¿Estás seguro de eliminar el dato selecionado?");

            if(respuesta == true){
                return true;
            }
            else{
                return false;
            }
        }
    </script>
    <body class="estudiante">
        <header>
            <img class='imagen1' src="imagenes/escudo.png" alt="icono">
            <img class='imgest2' src="imagenes/escudo.png" alt="icono">
            <div><h2 class='titulo'>Registrar un estudiante</h2></div>
        </header>
        <article>
            <p class='enunciado'>En esta seccion podras registrar un estudiante a la Institución Educativa Bosques de Pinares. Si no lo deseas, puedes <a href='index.html'>volver.</a>
                <br>
                <br>
            </p>
            <p class="required"><i>(Todos los campos con * son obligatorios)</i></b>
            
            <form action="#" method="POST">          
                <label for="cod">Código del estudiante*</label>
                <br>
                <input type="number" required placeholder="Ingresa el código del estudiante" name="codestud" id="cod">

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
                <input type="text" required placeholder="Ingresa el número de documento" name="numdocestud" id="numdoc">

                <br><br>

                <label for="grado">Grado del estudiante</label>
                <br>
                <input type="text" required placeholder="Ingresa a que grado entrará el estudiante" name="gradoestud" id="grado">
                
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
                <input type="text" required placeholder="Ingresa tu nombre" name="primnomestud" id="primnom">

                <br><br>

                <label for="segnom">Segundo nombre</label>
                <br>
                <input type="text" placeholder="Ingresa tu segundo nombre" name="segnomestud" id="segnom">

                <br><br>

                <label for="primape">Primer apellido*</label>
                <br>
                <input type="text" required placeholder="Ingresa tu primer apellido" name="primapellestud" id="primape">

                <br><br>

                <label for="segape">Segundo apellido*</label>
                <br>
                <input type="text" required placeholder="Ingresa tu segundo apellido" name="segapellestud" id="segape">

                <br><br>

                <label for="nac">Fecha de nacimiento*</label>
                <br>
                <input class="fechanac" type="date" required placeholder="Ingresa tu fecha de nacimiento" name="fecnacestud" id="nac">

                <br><br>

                <label for="lugnac">Lugar de nacimiento*</label>
                <br>
                <input type="text" required placeholder="Ingresa tu lugar de nacimiento" name="lugnacestud" id="lugnac">

                <br><br>

                <label for="direccion">Dirección*</label>
                <br>
                <input type="text" required placeholder="Ingresa la dirección de tu residencia" name="direcestud" id="direccion">

                <br><br>

                <label for="cel">Celular del estudiante</label>
                <br>
                <input type="text" placeholder="Ingresa tu número telefónico" name="celestud" id="cel">

                <br><br>

                <label for="enfermedad">Enfermedad o discapacidad permanente</label>
                <br>
                <input type="text" placeholder="Ingresa una enfermedad o discapacidad" name="enfermedad" id="enfermedad">

                <br><br>

                <label for="medi">Medicamento permanente</label>
                <br>
                <input type="text" placeholder="Ingresa un medicamento permanente" name="medipermestud" id="medi">

                <br><br>

                <label for="tiposangre">Tipo de sangre*</label>
                <br>
                <input type="text" required placeholder="Ingresa tu tipo de sangre" name="tiposangre" id="tiposangre">

                <br><br>

                <label for="eps">Eps*</label>
                <br>
                <input type="text" required placeholder="Ingresa tu eps" name="tipoeps" id="eps">

                <br><br>

                <br><br>

                <p class='penviar'><input class='enviar' type="submit" name="enviar" value="Registrar Estudiante"></p>
                <p class="preset"><input class="reset" type="reset" value="Restablecer Formulario"></p>
            </form>
            <button id="btn">Datos 👀</button>
        </article>
<?php
    if(isset($_POST['enviar'])){
        $codestud =$_POST["codestud"];
        $numdocestud =$_POST["numdocestud"];
        $primnomestud =$_POST["primnomestud"];
        $segnomestud =$_POST["segnomestud"];
        $primapellestud =$_POST["primapellestud"];
        $segapellestud =$_POST["segapellestud"];
        $fecnacestud =$_POST["fecnacestud"];
        $lugnacestud =$_POST["lugnacestud"];
        $gradoestud =$_POST["gradoestud"];
        $direcestud =$_POST["direcestud"];
        $celestud =$_POST["celestud"];
        $medipermestud =$_POST["medipermestud"];
        $tipodocumento =$_POST["tipodocumento"];
        $enfermedad =$_POST["enfermedad"];
        $genero =$_POST["genero"];
        $tipoeps =$_POST["tipoeps"];
        $tiposangre =$_POST["tiposangre"];
        
        $insertardatos = "INSERT INTO estudiante (codestud,numdocestud,primnomestud,segnomestud,primapellestud,segapellestud,fecnacestud,lugnacestud,gradoestud,direcestud,celestud,medipermestud,tipodocumento,enfermedad,genero,tipoeps,tiposangre) 
                                                 VALUES('$codestud',
                                                        '$numdocestud',
                                                        '$primnomestud',
                                                        '$segnomestud',
                                                        '$primapellestud',
                                                        '$segapellestud',
                                                        '$fecnacestud',
                                                        '$lugnacestud',
                                                        '$gradoestud',
                                                        '$direcestud',
                                                        '$celestud',
                                                        '$medipermestud',
                                                        '$tipodocumento',
                                                        '$enfermedad',
                                                        '$genero',
                                                        '$tipoeps',
                                                        '$tiposangre')";

        $ejecutarinsertar = mysqli_query($enlace, $insertardatos);

        if($ejecutarinsertar){
            echo"<script>alert('Se ha registrado correctamente')</script>";
            echo"<script>window.location.replace('docente.php')</script>";
        } elseif(!$ejecutarinsertar){
            echo"<script>alert('Presentamos problemas, no se ha podido registrar la información.')</script>";
            echo"<script>window.location.replace('docente.php')</script>";
        }
    }
?>
    <div class="caja" id="caja">        
        <table class="tablaest">
            <thead>
                <tr>
                    <th><p>CÓDIGO</p></th>
                    <th><p>NÚMERO DE DOCUMENTO</p></th>
                    <th><p>PRIMER NOMBRE</p></th>
                    <th><p>SEGUNDO NOMBRE</p></th>
                    <th><p>PRIMER APELLIDO</p></th>
                    <th><p>SEGUNDO APELLIDO</p></th>
                    <th><p>FECHA DE NACIMIENTO</p></th>
                    <th><p>LUGAR DE NACIMIENTO</p></th>
                    <th><p>GRADO</p></th>
                    <th><p>DIRECCIÓN</p></th>
                    <th><p>CELULAR</p></th>
                    <th><p>MEDICAMENTO PERMANENTE</p></th>
                    <th><p>TIPO DE DOCUMENTO</p></th>
                    <th><p>ENFERMEDAD PERMANENTE</p></th>
                    <th><p>GÉNERO</p></th>
                    <th><p>EPS</p></th>
                    <th><p>TIPO DE SANGRE</p></th>
                    <th><p>ID</p></th>
                    <th><p>EDITAR</p></th>
                    <th class="borrarth"><p>BORRAR</p></th>
                </tr>
            </thead>
        <?php
            $consulta = "SELECT * FROM estudiante";
            $ejecutar = mysqli_query($enlace, $consulta);
            
            $i=0;

            while ($row = mysqli_fetch_array($ejecutar)){
        ?>
        <tbody>        
                <tr>
                    <td><?= $row['codestud'] ?></td>
                    <td><?= $row['numdocestud'] ?></td>
                    <td><?= $row['primnomestud'] ?></td>
                    <td><?= $row['segnomestud'] ?></td>
                    <td><?= $row['primapellestud'] ?></td>
                    <td><?= $row['segapellestud'] ?></td>
                    <td><?= $row['fecnacestud'] ?></td>
                    <td><?= $row['lugnacestud'] ?></td>
                    <td><?= $row['gradoestud'] ?></td>
                    <td><?= $row['direcestud'] ?></td>
                    <td><?= $row['celestud'] ?></td>
                    <td><?= $row['medipermestud'] ?></td>
                    <td><?= $row['tipodocumento'] ?></td>
                    <td><?= $row['enfermedad'] ?></td>
                    <td><?= $row['genero'] ?></td>
                    <td><?= $row['tipoeps'] ?></td>
                    <td><?= $row['tiposangre'] ?></td>
                    <td><?= $row['idestud'] ?></td>
                    <td class="editartd"><a href="editar/editarest.php?idestud=<?= $row['idestud'] ?>">Editar</a></td>
                    <td class="borrartd"><a href="borrar/borrarest.php?idestud=<?= $row['idestud'] ?>"><button class="borrar" type='button' onclick="return ConfirmDelete()">X</button></a></td>
                </tr>
        </tbody>
            <?php } ?>
        </table>    
    <script src="js/activador.js"></script>

    <?php
        if(isset($_GET['editar'])){
            include 'editar/editarest.php';
        }
    ?>
    <?php
        if(isset($_GET['borrar'])){

            include 'borrar/borrarest.php';

            }
    ?>
</div>
</body>
        <div class="copy">
            <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
        </div>
</html>