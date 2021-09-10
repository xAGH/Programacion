/* Se importa la libreria de Scanner para solicitar mas facilmente
datos al usuario. */

import java.util.Scanner;

public class EntradaString{
    public static void main(String[] args){

        // Se crea un metodo que reciba los datos de teclado.
        Scanner entrada = new Scanner(System.in);

        // Se crea la variable que almacenara los datos.
        String cadena;

        // Se imprime un mensaje solicitando la cadena.
        System.out.print("Digite una cadena: ");

        /* Se iguala la entrada del teclado al metodo entrada con next el cual
        tomara todos los datos hasta encontrar un espacio, para evitar esto 
        se utiliza nextLine()
        cadena = entrada.next();          Recibe los datos de teclado, pero solo la primera palabra(hasta que encuentre un espacio)
        cadena = entrada.nextLine();      Recibe todo lo ingresado por teclado.
        */
        cadena = entrada.nextLine();

        System.out.println("La cadena es: " + cadena);
        
        // Se cierrra el metodo.
        entrada.close();
    }
}