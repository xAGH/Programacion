package Operadores;

public class Ternario {
    public static void main(String[] args) {
        // Se ejecuta la sentencia despues de ? si la condicion es verdadera, 
        //de lo contrario, se ejecuta la sentencia despues de los :
        var resultado = (3 > 2) ? "Verdadero" : "Falso"; 
        System.out.println("resultado = " + resultado);
    }
}
