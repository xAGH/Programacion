<?php
    include ("conexion.php");
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Eps</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel="shortcut icon" href="Imagenes/icono.jpg" type="image/png">
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
            <img class='imgeps1' src="imagenes/escudo.png" alt="icono">
            <img class='imgeps2' src="imagenes/escudo.png" alt="icono">
            <div><h2 class='titulo'>Agregar una Eps</h2></div>
        </header>
        <article>
            <p class='enunciado'>En esta seccion podras registrar una Eps a la Institución Educativa Bosques de Pinares. Si no lo deseas, puedes <a href='index.html'>volver.</a>
            <br>
            <br>
            </p>
            <p class="required"><i>(Todos los campos con * son obligatorios)</i></b>

            <form action="#" class="formeps" method="POST">

            <label for="nombre">Nombre de la Eps*</label>
            <br>
            <input type="text" required name="nombreeps" id="nombre" placeholder="Ingrese el nombre de la Eps">

            <p class='penviar'><input class='enviar' type="submit" name="enviar" value="Agregar Eps"></p>

            <p class="preset"><input class="reset" type="reset" value="Restablecer Formulario"></p>

            </form>
            <button id="btn">Datos 👀</button>
        </article>

<?php
    if(isset($_POST['enviar'])){
        $nombre =$_POST["nombreeps"];
        
        $insertardatos = "INSERT INTO eps (nombreeps) VALUES('$nombre')";

        $ejecutarinsertar = mysqli_query($enlace, $insertardatos);

        if($ejecutarinsertar){
            echo"<script>alert('Se ha registrado correctamente')</script>";
            echo"<script>window.location.replace('eps.php')</script>";
        } elseif(!$ejecutarinsertar){
            echo"<script>alert('Presentamos problemas, no se ha podido registrar la información.')</script>";
            echo"<script>window.location.replace('eps.php')</script>";
        }
    }
?>
 <div class="caja" id="caja">        
        <table class="tabla">
            <thead>
                <tr>
                    <th><p>ID</p></th>
                    <th><p>NOMBRE DE LA EPS</p></th>
                    <th><p>EDITAR</p></th>
                    <th class="borrarth"><p>BORRAR</p></th>
                </tr>
            </thead>
        <?php
            $consulta = "SELECT * FROM eps";
            $ejecutar = mysqli_query($enlace, $consulta);
            
            $i=0;

            while ($row = mysqli_fetch_array($ejecutar)){
        ?>
        <tbody>
                <tr>
                    <td><?= $row['ideps'] ?></td>
                    <td><?= $row['nombreeps'] ?></td>
                    <td class="editartd"><a href="editar/editareps.php?ideps=<?= $row['ideps'] ?>">Editar</a></td>
                    <td class="borrartd"><a href="borrar/borrareps.php?ideps=<?= $row['ideps'] ?>"><button class="borrar" type='button' onclick="return ConfirmDelete()">X</button></a></td>
                </tr>
        </tbody>
            <?php } ?>
        </table>    
    <script src="js/activador.js"></script>

    <?php
        if(isset($_GET['editar'])){
            include 'editar/editareps.php';
        }
    ?>
    <?php
        if(isset($_GET['borrar'])){

            include 'borrar/borrareps.php';

            }
    ?>
    </div>
</body>
    <div class="copy">
        <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
    </div>
</html>