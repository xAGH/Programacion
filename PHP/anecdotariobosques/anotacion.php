<?php
    include ("conexion.php");
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" href="Imagenes/icono.jpg" type="image/png">
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Anotación</title>
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
    <body>
        <header>
            <img class='imagen1' src="imagenes/escudo.png" alt="icono">
            <img class='imganot2' src="imagenes/escudo.png" alt="icono">
            <div><h2 class='titulo'>Agregar una anotación</h2></div>
        </header>
        <article>
            <p class='enunciado'>En esta seccion podrás agrgar una anotación a un <a href="estudiante.php">estuadiante</a> de la Institución Educativa Bosques de Pinares. Si no lo deseas, puedes <a href='index.html'>volver.</a>
                <br>
                <br>
            (Para añadir una anotación deberás saber el código de falta, si lo desconoces puedes verlo aquí <a target="blank"href="visualizar_falta.php">Código de las faltas</a>)
            </p>
            <p class="required"><i>(Todos los campos con * son obligatorios)</i></b>
                <form action="#" method="POST">      

                    <label for="cod">Código de la anotación*:</label>
                    <br>
                    <input type="number" required placeholder="Ingresa el código de la anotación" name="codanot" id="cod">
    
                    <br><br>
    
                    <label for="fecha">Fecha de la anotación*</label>
                    <br>
                    <input type="date" required placeholder="Ingrese la fecha de la anotacion" name="fechaanot" id="fecha">
                    
                    <br><br>

                    <label for="des">Descripción de la anotación*</label>
                    <br>
                    <textarea name="desc" id="des" class="textarea" placeholder="Indica en qué consistió la falta" required></textarea>

                    <br><br>

                    <label for="estud">Código del estudiante*</label>
                    <br>
                    <input type="number" required placeholder="Ingresa el código del estudiante" name="idestud" id="estud"> 

                    <br><br>

                    <label for="profe">Código del profesor*</label>
                    <br>
                    <input type="number" required placeholder="Ingresa el código del profesor" name="codprofe" id="profe">

                    <br><br>

                    <label for="asignatura">Código de la asignatura*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el código de la asignatura" name="codasig" id="asignatura">

                    <br><br>

                    <label for="falta">Código de la falta*</label>
                    <br>
                    <input type="number" required placeholder="Ingresa el código de la falta" name="codfalta" id="falta">

                    <br><br>

                    <p class='penviar'><input class='enviar' type="submit" name="enviar" value="Registrar Anotación"></p>
                    <p class="preset"><input class="reset" type="reset" value="Restablecer Formulario"></p>
                </form>
                <button id="btn">Datos 👀</button>
            </article>
        
<?php
    if(isset($_POST['enviar'])){
        $codanot =$_POST["codanot"];
        $fecha =$_POST["fechaanot"];
        $desc =$_POST['desc'];
        $estud =$_POST["idestud"];
        $profe =$_POST["codprofe"];
        $asig =$_POST["codasig"];
        $falta =$_POST["codfalta"];
        
        $insertardatos = "INSERT INTO anotacion (codanotacion,fechaanotacion,descrianotacion,idestud,codprofe,codasignatura,codtipofalta) 
                                                 VALUES('$codanot',
                                                        '$fecha',
                                                        '$desc',
                                                        '$estud',
                                                        '$profe',
                                                        '$asig',
                                                        '$falta')";

        $ejecutarinsertar = mysqli_query($enlace, $insertardatos);

        if($ejecutarinsertar){
            echo"<script>alert('Se ha registrado correctamente')</script>";
            echo"<script>window.location.replace('anotacion.php')</script>";
        } elseif(!$ejecutarinsertar){
            echo"<script>alert('Presentamos problemas, no se ha podido registrar la información.')</script>";
            echo"<script>window.location.replace('anotacion.php')</script>";
        }
    }
?>
 <div class="caja" id="caja">        
        <table>
            <thead>
                <tr>
                    <th><p>ID</p></th>
                    <th><p>CÓDIGO ANOTACIÓN</p></th>
                    <th><p>FECHA ANOTACIÓN</p></th>
                    <th><p>DESCRIPCIÓN</p></th>
                    <th><p>ID DEL ESTUDIANTE</p></th>
                    <th><p>CÓDIGO DEL DOCENTE</p></th>
                    <th><p>CÓDIGO DE LA ASIGNATURA</p></th>
                    <th><p>CÓDIGO DE LA FALTA</p></th>
                    <th><p>EDITAR</p></th>
                    <th class="borrarth"><p>BORRAR</p></th>
                </tr>
            </thead>
        <?php
            $consulta = "SELECT * FROM anotacion";
            $ejecutar = mysqli_query($enlace, $consulta);
            
            $i=0;

            while ($row = mysqli_fetch_array($ejecutar)){
        ?>
        <tbody>
                <tr>
                    <td><?= $row['idanotacion'] ?></td>
                    <td><?= $row['codanotacion'] ?></td>
                    <td><?= $row['fechaanotacion'] ?></td>
                    <td><?= $row['descrianotacion'] ?></td>
                    <td><?= $row['idestud'] ?></td>
                    <td><?= $row['codprofe'] ?></td>
                    <td><?= $row['codasignatura'] ?></td>
                    <td><?= $row['codtipofalta'] ?></td>
                    <td class="editartd"><a href="editar/editaranot.php?idanotacion=<?= $row['idanotacion'] ?>">Editar</a></td>
                    <td class="borrartd"><a href="borrar/borraranot.php?idanotacion=<?= $row['idanotacion'] ?>"><button class="borrar" type='button' onclick="return ConfirmDelete()">X</button></a></td>
                </tr>
        </tbody>
            <?php } ?>
        </table>    
    <script src="js/activador.js"></script>

    <?php
        if(isset($_GET['editar'])){
            include 'editar/editaranot.php';
        }
    ?>
    <?php
        if(isset($_GET['borrar'])){

            include 'borrar/borraranot.php';

            }
    ?>
</div>

</body>
        <div class="copy">
            <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
        </div>
</html>