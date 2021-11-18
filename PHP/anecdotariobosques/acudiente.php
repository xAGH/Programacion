<?php
    include ("conexion.php");
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="shortcut icon" href="Imagenes/icono.jpg" type="image/png">
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Acudiente</title>
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
    <body class="acudiente">
        <header>
            <img class='imagen1' src="imagenes/escudo.png" alt="icono">
            <img class='imgacu2' src="imagenes/escudo.png" alt="icono">
            <div><h2 class='titulo'>Registrar a un acudiente</h2></div>
        </header>
        <article>
            <p class='enunciado'>En esta seccion podrás resgistrar un acudiente a la Institución Educativa Bosques de Pinares. Si no lo deseas, puedes <a href='index.html'>volver</a>.
                <br>
                <br>
            </p>

            <p class="required"><i>(Todos los campos con * son obligatorios)</i></b>
                <form action="#" method="POST">

                    <label for="codigo">Número de documento del acudiente*</label>       
                    <br>  
                    <input type="number" required placeholder="Ingresa el número de documento del acudiente" name="doc" id="codigo">
                    
                    <br><br>

                    <label for="nombre">Nombre del acudiente*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el nombre del acudiente" name="nom" id="nombre">

                    <br><br>

                    <label for="direccion">Dirección del acudiente*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa la dirección del acudiente" name="direc" id="direccion">

                    <br><br>

                    <label for="telefono">Número telefónico*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el número telefónico del acudiente" name="tele" id="telefono">

                    <br><br>
                 
                    <label for="correo">Correo*</label>
                    <br>
                    <input type="email" required placeholder="Ingresa el E-mail del acudiente" name="email" id="correo">

                    <br><br>

                    <label for="sexo">Genero*</label>
                    <select name="genero"  id="sexo">
                        <option value="Masculino">Masculino</option>
                        <option value="Femenino">Femenino</option>
                        <option value="Prefiero no decirlo">Prefiero no decirlo</option>
                        <option value="Otro">Otro</option>
                    </select>

                    <br><br>

                    <p class='penviar'><input class='enviar' type="submit" name="enviar" value="Registrar Acudiente"></p>
                    <p class="preset"><input class="reset" type="reset" value="Restablecer Formulario"></p>
                </form>
                <button id="btn">Datos 👀</button>
            </article>
<?php
    if(isset($_POST['enviar'])){
        $doc =$_POST["doc"];
        $nom =$_POST["nom"];
        $direc =$_POST["direc"];
        $tele =$_POST["tele"];
        $email =$_POST["email"];
        $gen =$_POST["genero"];

        $insertardatos = "INSERT INTO acudiente (numero_documento, nomacudiente, diracudiente, telacudiente, correoacudiente, genero, idacudiente)
                                                 VALUES('$doc',
                                                        '$nom',
                                                        '$direc',
                                                        '$tele',
                                                        '$email',
                                                        '$gen',
                                                        '$id')";

        $ejecutarinsertar = mysqli_query($enlace, $insertardatos);

        if($ejecutarinsertar){
            echo"<script>alert('Se ha registrado correctamente')</script>";
            echo"<script>window.location.replace('acudiente.php')</script>";
        } elseif(!$ejecutarinsertar){
            echo"<script>alert('Presentamos problemas, no se ha podido registrar la información.')</script>";
            echo"<script>window.location.replace('acudiente.php')</script>";
        }
    }
?>
    <div class="caja" id="caja">        
        <table>
            <thead>
                <tr>
                    <th><p>NÚMERO DE DOCUMENTO</p></th>
                    <th><p>NOMBRE</p></th>
                    <th><p>DIRECCION</p></th>
                    <th><p>TELÉFONO</p></th>
                    <th><p>EMAIL</p></th>
                    <th><p>GÉNERO</p></th>
                    <th><p>EDITAR</p></th>
                    <th class="borrarth"><p>BORRAR</p></th>
                </tr>
            </thead>
        <?php
            $consulta = "SELECT * FROM acudiente";
            $ejecutar = mysqli_query($enlace, $consulta);
            
            $i=0;

            while ($row = mysqli_fetch_array($ejecutar)){
        ?>
        <tbody>
                <tr>
                    <td><?= $row['numero_documento'] ?></td>
                    <td><?= $row['nomacudiente'] ?></td>
                    <td><?= $row['diracudiente'] ?></td>
                    <td><?= $row['telacudiente'] ?></td>
                    <td><?= $row['correoacudiente'] ?></td>
                    <td><?= $row['genero'] ?></td>
                    <td class="editartd"><a href="editar/editaracu.php?numero_documento=<?= $row['numero_documento'] ?>">Editar</a></td>
                    <td class="borrartd"><a href="borrar/borraracu.php?numero_documento=<?= $row['numero_documento'] ?>"><button class="borrar" type='button' onclick="return ConfirmDelete()">X</button></a></td>
                </tr>
        </tbody>
            <?php } ?>
        </table>    
    <script src="js/activador.js"></script>

    <?php
        if(isset($_GET['editar'])){
            include 'editar/editaracu.php';
        }
    ?>
    <?php
        if(isset($_GET['borrar'])){

            include 'borrar/borraracu.php';

            }
    ?>
</div>
</body>
    <div class="copy">
        <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
    </div>
</html>