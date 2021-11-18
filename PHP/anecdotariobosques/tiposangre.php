<?php
    include ("conexion.php");
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Tipo De Sangre</title>
        <meta name='viewport' content='width= device-width, initial-scale=1'>
        <link href="https://fonts.googleapis.com/css2?family=Kufam&display=swap" rel="stylesheet">
        <link rel="shortcut icon" href="imagenes/icono.jpg" type="image/png"> 
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
            <img class='imgsan2' src="imagenes/escudo.png" alt="icono">
            <div class='titulo'><h2>Agregar un Tipo de sangre</h2></div>
        </header>
        
        <article>

            <p class='enunciado'>En esta seccion podras agregar un Tipo de sangre. Si no lo deseas, puedes <a href='index.html'>volver.</a>
            <br>
            <br>
            </p>
            <p class="required"><i>(Todos los campos con * son obligatorios)</i></b>

            <form action="#" class="formsan" method="POST">

                <label for="nombre">Nombre del tipo de sangre*</label>
                <br>
                <input type="text" required name="sangre" id="nombre" placeholder="Ingrese el nombre del tipo de sangre">
               
                <br><br>

                <p class='penviar'><input class='enviar' type="submit" name="enviar" value="Agregar Tipo de sangre"></p>

                <p class="preset"><input class="reset" type="reset" value="Restablecer Formulario"></p>

            </form>
            <button id="btn">Datos 👀</button>
        </article>
<?php
    if(isset($_POST['enviar'])){
        $sangre =$_POST["sangre"];
        
        $insertardatos = "INSERT INTO tiposangre (nomtiposangre) VALUES('$sangre')";

        $ejecutarinsertar = mysqli_query($enlace, $insertardatos);

        if($ejecutarinsertar){
            echo"<script>alert('Se ha registrado correctamente')</script>";
            echo"<script>window.location.replace('tiposangre.php')</script>";
        } elseif(!$ejecutarinsertar){
            echo"<script>alert('Presentamos problemas, no se ha podido registrar la información.')</script>";
            echo"<script>window.location.replace('tiposangre.php')</script>";
        }
    }
?>
    <div class="caja" id="caja">        
        <table class="tabla">
            <thead>
                <tr>
                    <th><p>ID</p></th>
                    <th><p>TIPO DE SANGRE</p></th>
                    <th><p>EDITAR</p></th>
                    <th class="borrarth"><p>BORRAR</p></th>
                </tr>
            </thead>
        <?php
            $consulta = "SELECT * FROM tiposangre";
            $ejecutar = mysqli_query($enlace, $consulta);
            
            $i=0;

            while ($row = mysqli_fetch_array($ejecutar)){
        ?>
        <tbody>
                <tr>
                    <td><?= $row['idtiposangre'] ?></td>
                    <td><?= $row['nomtiposangre'] ?></td>
                    <td class="editartd"><a href="editar/editarsan.php?idtiposangre=<?= $row['idtiposangre'] ?>">Editar</a></td>
                    <td class="borrartd"><a href="borrar/borrarsan.php?idtiposangre=<?= $row['idtiposangre'] ?>"><button class="borrar" type='button' onclick="return ConfirmDelete()">X</button></a></td>
                </tr>
        </tbody>
            <?php } ?>
        </table>    
    <script src="js/activador.js"></script>

    <?php
        if(isset($_GET['editar'])){
            include 'editar/editarsan.php';
        }
    ?>
    <?php
        if(isset($_GET['borrar'])){

            include 'borrar/borrarsan.php';

            }
    ?>
    </div>
    </body>
        <div class="copy">
            <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
        </div>
</html>

