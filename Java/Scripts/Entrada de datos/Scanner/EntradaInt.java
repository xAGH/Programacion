/* Se importa la libreria de Scanner para solicitar mas facilmente
datos al usuario. */

import java.util.Scanner;

public class EntradaInt{
    public static void main(String[] args){

        // Se crea un metodo que reciba los datos de teclado.
        Scanner entrada = new Scanner(System.in);

        // Se crea la variable que almacenara los datos.
        int numero;

        // Se imprime un mensaje solicitando el numero.
        System.out.print("Digite un numero: ");

        // Se iguala la entrada del numero a la variable creada.
        numero = entrada.nextInt();

        System.out.println("El numero es: " + numero);
        
        // Se cierrra el metodo.
        entrada.close();
    }
}