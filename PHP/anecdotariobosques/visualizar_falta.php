<?php
    include ("conexion.php");
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" href="Imagenes/icono.jpg" type="image/png">
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Visualizar Tipos De Faltas</title>
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
        <p class="enunciado_visualizar">Si quieres agregar un tipo de falta, haz click <a href="tipofalta.php">aquí</a></p>
<div class="visualizar_falta">        
        <table class="tabla">
            <thead>
                <tr>
                    <th><p>CÓDIGO</p></th>
                    <th><p>NOMBRE</p></th>
                    <th><p>DESCRIPCIÓN</p></th>
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
        <p class="pvolver"><a href="anotacion.php" class="volver_falta">Volver</a></p>
</div>

</body>
        <div class="copy">
            <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
        </div>
</html>