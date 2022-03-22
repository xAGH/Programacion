function Funcion(){
    var texto;
    var usuario = prompt("Por favor ingresa tu nombre: ");
    if (usuario === null || usuario === ""){
        texto = "EL usuario ha cancelado la ingresión de datos.";
    }
    else{
        texto = "Hola " + usuario + ", bienvenido.";
    }
    document.getElementById("texto").innerHTML = texto;
}