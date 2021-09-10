<?php
    include ("conexion.php");
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" href="Imagenes/icono.jpg" type="image/png">
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Tipo de Falta</title>
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
            <img class='imgfal2' src="imagenes/escudo.png" alt="icono">
            <div><h2 class='titulo'>Añadir un tipo de falta</h2></div>
        </header>
        <article>
            <p class='enunciado'>En esta seccion podrás agregar un tipo de falta para una próxima anotación de la Institución Educativa Bosques de Pinares. Si no lo deseas, puedes <a href='index.html'>volver.</a>
                <br>
                <br>
            </p>
            <p class="required"><i>(Todos los campos con * son obligatorios)</i></b>
                <form action="#" method="POST">      

                    <label for="nom">Nombre de la falta*:</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el nombre de la falta" name="falta" id="nom">
    
                    <br><br>
    
                    <label for="descrip">Descripción de la falta*</label>
                    <br>
                    <input type="text" required placeholder="Describa la falta" name="descripcion" id="descrip">

                    <br><br>

                    <label for="tip">Código de la falta*</label>
                    <br>
                    <input type="text" required placeholder="Ingrese el tipo de falta" name="id" id="tip">

                    <br><br>

                    <p class='penviar'><input class='enviar' type="submit" name="enviar" value="Agregar Tipo de Falta"></p>
                    <p class="preset"><input class="reset" type="reset" value="Restablecer Formulario"></p>
                </form>
                <button id="btn">Datos 👀</button>
            </article>
            
<?php
    if(isset($_POST['enviar'])){
        $nom =$_POST["falta"];
        $desc =$_POST["descripcion"];
        $id =$_POST["id"];
        
        $insertardatos = "INSERT INTO tipofalta (nomtipofalta,descriptipofalta,idtipofalta) 
                                                 VALUES('$nom',
                                                        '$desc',
                                                        '$id')";

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
        <table class="tabla">
            <thead>
                <tr>
                    <th><p>CÓDIGO</p></th>
                    <th><p>NOMBRE</p></th>
                    <th><p>DESCRIPCIÓN</p></th>
                    <th><p>EDITAR</p></th>
                    <th class="borrarth"><p>BORRAR</p></th>
                </tr>
            </thead>
        <?php
            $consulta = "SELECT * FROM tipofalta";
            $ejecutar = mysqli_query($enlace, $consulta);
            
            $i=0;

            while ($row = mysqli_fetch_array($ejecutar)){
        ?>
        <tbody>
                <tr>
                    <td><?= $row['idtipofalta'] ?></td>
                    <td><?= $row['nomtipofalta'] ?></td>
                    <td><?= $row['descriptipofalta'] ?></td>
                    <td class="editartd"><a href="editar/editaranot.php?idtipofalta=<?= $row['idtipofalta'] ?>">Editar</a></td>
                    <td class="borrartd"><a href="borrar/borraranot.php?idtipofalta=<?= $row['idtipofalta'] ?>"><button class="borrar" type='button' onclick="return ConfirmDelete()">X</button></a></td>
                </tr>
        </tbody>
            <?php } ?>
        </table>    
    <script src="js/activador.js"></script>

    <?php
        if(isset($_GET['editar'])){
            include 'editar/editarfal.php';
        }
    ?>
    <?php
        if(isset($_GET['borrar'])){

            include 'borrar/borrarfal.php';

            }
    ?>
</div>

</body>
        <div class="copy">
            <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
        </div>
</html>