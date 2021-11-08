package Operadores;

public class IgualdadRelacionales {
    
    public static void main(String[] args) {
        // OPERADORES DE IGUALDAD
        var a = 3;
        var b = 2;
        
        var c = (a == b);
        System.out.println("c = " + c);
        
        var d = a != b; // El uso de parentesis solo es por temas de legibilidad
        System.out.println("d = " + d);
        
        var cadena1 = "Hola";
        var cadena2 = "Adios";
        var e = cadena1 == cadena2; // No compara el contenido sino la referencia del objeto
        System.out.println("e = " + e);
        
        var f = cadena1.equals(cadena2); // Compara el contenido de cadenas.
        System.out.println("f = " + f);

        // OPERADORES RELACIONALES
        var g = a > b; // Mayor que > o el mayor o igual >=
        System.out.println("g = " + g);
        
        var h = a < b; // Menor que > o el menor o igual >=
        System.out.println("h = " + h);
    }
}
