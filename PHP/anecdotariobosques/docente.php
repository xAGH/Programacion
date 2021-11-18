<?php
    include ("conexion.php");
?>
<!DOCTYPE html>
    <html>
        <head>
            <link rel="shortcut icon" href="imagenes/icono.jpg" type="image/png">
            <meta charset='utf-8'>
            <meta http-equiv='X-UA-Compatible' content='IE=edge'>
            <title>Docente</title>
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
        <body class="docente">
            <header>
                <img class='imagen1' src="imagenes/escudo.png" alt="icono">
                <img class='imgdoc2' src="imagenes/escudo.png" alt="icono">
                <div><h2 class='titulo'>Registrar a un docente</h2></div>
            </header>
            <article>
                <p class='enunciado'>En esta seccion podrás resgistrar un docente a la Institución Educativa Bosques de Pinares. Si no lo deseas, puedes <a href='index.html'>volver</a>.
                    <br>
                    <br>
                </p>
                <p class="required"><i>(Todos los campos con * son obligatorios)</i></b>
                    <form action="#" method="POST">
                        <label for="codi">Código del docente*</label>       
                        <br>  
                        <input type="number" required placeholder="Ingresa el código del docente" name="cod" id="codi">
                    
                    <br><br>

                    <label for="tipo">Genero*</label>
                    <select name="doc"  id="tipo">
                        <option value="Masculino">Masculino</option>
                        <option value="Femenino">Femenino</option>
                        <option value="Prefiero no decirlo">Prefiero no decirlo</option>
                    </select>

                    <br><br>

                    <label for="num">Número de documento*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el número de documento" name="nume" id="num">

                    <br><br>

                    <label for="primapell">Primer apellido*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el primer apellido" name="prim" id="primapell">
                    
                    <br><br>

                    <label for="segapell">Segundo apellido*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el segundo apellido" name="seg" id="segapell">

                    <br><br>

                    <label for="nombre">Primer nombre*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa el primer nombre" name="nom" id="nombre">

                    <br><br>

                    <label for="nombre2">Segundo nombre</label>
                    <br>
                    <input type="text" placeholder="Ingresa el segundo nombre" name="nom2" id="nombre2">

                    <br><br>

                    <label for="email">E-mail*</label>
                    <br>
                    <input type="email" required placeholder="Ingrese su E-mail" name="email" id="email">

                    <br><br>
                    
                    <label for="asig">Asignatura otorgada*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa la asignatura otrogada" name="asig" id="asig">

                    <br><br>

                    <label for="sexo">Genero*</label>
                    <select name="genero"  id="sexo">
                        <option value="Masculino">Masculino</option>
                        <option value="Femenino">Femenino</option>
                        <option value="Prefiero no decirlo">Prefiero no decirlo</option>
                    </select>

                    <br><br>

                    <label for="sede">Sede asignada*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa tu sede" name="sede" id="sede">
                    
                    <br><br>

                    <label for="celular">Número de teléfono*</label>
                    <br>
                    <input type="text" required placeholder="Ingresa tu número telefónico" name="cel" id="celular">

                    <br><br>

                    <p class='penviar'><input class='enviar' type="submit" name="enviar" value="Registrar Docente"></p>
                    <p class="preset"><input class="reset" type="reset" value="Restablecer Formulario"></p>
                </form>
        </article>
        <button id="btn">Datos 👀</button>
<?php
    if(isset($_POST['enviar'])){
        $cod =$_POST["cod"];
        $doc =$_POST["doc"];
        $numdoc =$_POST["nume"];
        $primapell =$_POST["prim"];
        $segapell =$_POST["seg"];
        $nombre =$_POST["nom"];
        $nombre2 =$_POST["nom2"];
        $email =$_POST["email"];
        $asignatura  =$_POST["asig"];
        $genero =$_POST["genero"];
        $sede =$_POST["sede"];
        $cel =$_POST["cel"];

        $insertardatos = "INSERT INTO profesor (tipodocprofe,numdocprofe,primapellprofe,segapellprofe,primnomprofe, segnomprofe, emailprofe,asignaturaprofe, generoprofe,sedeprofe,celprofe, codprofe)
                                                 VALUES('$doc',
                                                        '$numdoc',
                                                        '$primapell',
                                                        '$segapell',
                                                        '$nombre',
                                                        '$nombre2',
                                                        '$email',
                                                        '$asignatura',
                                                        '$genero',
                                                        '$sede',
                                                        '$cel', 
                                                        '$cod')";

        $ejecutarinsertar = mysqli_query($enlace, $insertardatos);

        if($ejecutarinsertar){
            echo"<script>alert('Se ha registrado correctamente')</script>";
            echo"<script>window.location.replace('docente.php')</script>";
        } elseif(!$ejecutarinsertar){
            echo"<script>alert('¡Ya existe un docente con ese código!')</script>";
            echo"<script>window.location.replace('docente.php')</script>";
        }
    }
?>
    <div class="caja" id="caja">        
        <table class="tabladoc">
            <thead>
                <tr>
                    <th><p>CÓDIGO</p></th>
                    <th><p>DOCUMENTO</p></th>
                    <th><p>NÚMERO DE DOCUMENTO</p></th>
                    <th><p>PRIMER APELLIDO</p></th>
                    <th><p>SEGUNDO APELLIDO</p></th>
                    <th><p>PRIMER NOMBRE</p></th>
                    <th><p>SEGUNDO NOMBRE</p></th>
                    <th><p>EMAIL</p></th>
                    <th><p>ASIGNATURA</p></th>
                    <th><p>GÉNERO</p></th>
                    <th><p>SEDE</p></th>
                    <th><p>NÚMERO TELEFÓNICO</p></th>
                    <th><p>EDITAR</p></th>
                    <th class="borrarth"><p>BORRAR</p></th>
                </tr>
            </thead>
        <?php
            $consulta = "SELECT * FROM profesor";
            $ejecutar = mysqli_query($enlace, $consulta);
            
            $i=0;

            while ($row = mysqli_fetch_array($ejecutar)){
        ?>
        <tbody>        
                <tr>
                    <td><?= $row['codprofe'] ?></td>
                    <td><?= $row['tipodocprofe'] ?></td>
                    <td><?= $row['numdocprofe'] ?></td>
                    <td><?= $row['primapellprofe'] ?></td>
                    <td><?= $row['segapellprofe'] ?></td>
                    <td><?= $row['primnomprofe'] ?></td>
                    <td><?= $row['segnomprofe'] ?></td>
                    <td><?= $row['emailprofe'] ?></td>
                    <td><?= $row['asignaturaprofe'] ?></td>
                    <td><?= $row['generoprofe'] ?></td>
                    <td><?= $row['sedeprofe'] ?></td>
                    <td><?= $row['celprofe'] ?></td>
                    <td class="editartd"><a href="editar/editardoc.php?codprofe=<?= $row['codprofe'] ?>">Editar</a></td>
                    <td class="borrartd"><a href="borrar/borrardoc.php?codprofe=<?= $row['codprofe'] ?>"><button class="borrar" type='button' onclick="return ConfirmDelete()">X</button></a></td>
                </tr>
        </tbody>
            <?php } ?>
        </table>    
    <script src="js/activador.js"></script>

    <?php
        if(isset($_GET['editar'])){
            include 'editar/editardoc.php';
        }
    ?>
    <?php
        if(isset($_GET['borrar'])){

            include 'borrar/borrardoc.php';

            }
    ?>
</div>
</body>
        <div class="copy">
            <center>&copy;Página realizada por Alejandro Giraldo Herrera, todos los derechos reservados 2020</center>
        </div>
</html>