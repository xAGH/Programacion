/* Se importa la libreria de Scanner para solicitar mas facilmente
datos al usuario. */

import java.util.Scanner;

// NOTA: EN LAS ENTRADAS DE NUMEROS REALES, LA PARTE DECIMAL SE DEFINE CON UNA COME EN VEZ DE CON UN PUNTO. 

public class EntradaDouble{
    public static void main(String[] args){

        // Se crea un metodo que reciba los datos de teclado.
        Scanner entrada = new Scanner(System.in);

        // Se crea la variable que almacenara los datos.
        double decimal;

        // Se imprime un mensaje solicitando el decimal.
        System.out.print("Digite un decimal: ");

        // Se iguala la entrada del decimal a la variable creada.
        decimal = entrada.nextDouble();

        System.out.println("El numero es: " + decimal);
        
        // Se cierrra el metodo.
        entrada.close();
    }
}