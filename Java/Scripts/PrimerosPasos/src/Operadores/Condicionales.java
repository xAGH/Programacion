package Operadores;

public class Condicionales {
    public static void main(String[] args) {
        var a = 10;
        var valorMinimo = 0;
        var valorMaximo = 10;
        
        var resultadoY = a >= valorMinimo && a <= valorMaximo; // Operador condicional 'y'
        System.out.println("resultado = " + resultadoY);
    
        var resultadoO = a >= valorMinimo || a <= valorMaximo; // Operador condicional 'o'
        System.out.println("resultadoO = " + resultadoO);
    }
}
