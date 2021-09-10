/* Se importa la libreria de Scanner para solicitar mas facilmente
datos al usuario. */

import java.util.Scanner;

public class EntradaChar{
    public static void main(String[] args){

        // Se crea un metodo que reciba los datos de teclado.
        Scanner entrada = new Scanner(System.in);

        // Se crea la variable que almacenara los datos.
        char caracter;

        // Se imprime un mensaje solicitando la cadena.
        System.out.print("Digite un caracter: ");

        // Se utiliza charAt para indicar que solo lea y almacene el primer caracter que encuentre. 
        
        caracter = entrada.next().charAt(0);

        System.out.println("EL caracter es: " + caracter);
        
        // Se cierrra el metodo.
        entrada.close();
    }
}