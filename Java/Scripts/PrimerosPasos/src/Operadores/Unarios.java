package Operadores;

public class Unarios {
    public static void main(String[] args) {
        var a = 3;
        var b = -a; // El valor de b sera el valor de a pero negativo
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        
        var c =  true;
        var d = !c; // Operador de negacion, d tomara el valor contrario de c. SOlo aplica a booleanos.
        System.out.println("c = " + c);
        System.out.println("d = " + d);
        
        // Incremento
        //1. Preincremento (simbolo antes de la variable)
        var e = 3;
        var f = ++e; // Primero incrementa la variable y despues se usa su valor
        System.out.println("e = " + e);
        System.out.println("f = " + f);
        //2. Postincremento (simbolo despues de la variable)
        var g = 5;
        var h = g++; // Primero se utiliza el valor de la vatiable y luego se incrementa.
        System.out.println("g = " + g);
        System.out.println("h = " + h);
        
        // Tambien se puede usar con los demas operadores aritmeticos
    }
}
