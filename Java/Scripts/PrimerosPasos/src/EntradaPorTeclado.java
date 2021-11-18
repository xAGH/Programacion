
import java.util.Scanner;

public class EntradaPorTeclado {

    public static void main(String[] args) {
        System.out.print("Escribe tu nombre: ");
        Scanner consola = new Scanner(System.in);
        var usuario = consola.nextLine();
        System.out.println("Usuario = " + usuario);
    }
}
