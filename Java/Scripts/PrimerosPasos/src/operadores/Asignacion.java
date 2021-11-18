package Operadores;

public class Asignacion {

    public static void main(String[] args) {
        int a = 3, b = 2;
        var c = a + 5 - b; // Operador de asignacion, asigna el resultado de la operacion de la derecha a la izquierda del =.
        System.out.println("c = " + c);

        a += 1; // a = a + 1
        System.out.println("a = " + a);

        a -= 1; // a = a - 1
        System.out.println("a = " + a);

        a *= 1; // a = a * 1
        System.out.println("a = " + a);

        a /= 1; // a = a / 1
        System.out.println("a = " + a);

        a %= 1; // a = a % 1
        System.out.println("a = " + a);
    }
}
