import java.util.Scanner;

public class OperadoresAritmeticos{
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        float numero1, numero2, suma, resta, mult, div, resto;
        
        System.out.print("Digite el numero #1: ");
        numero1 = entrada.nextFloat();
        System.out.print("Digite el numero #2: ");
        numero2 = entrada.nextFloat();

        suma = numero1 + numero2;
        resta = numero1 - numero2;
        mult = numero1 * numero2;
        div = numero1 / numero2;;
        resto = numero1 % numero2;

        System.out.println("La suma es: " + suma);
        System.out.println("La resta es: " + resta);
        System.out.println("La multiplicaion es: " + mult);
        System.out.println("La division es: " + div);
        System.out.println("El modulo es: " + resto);
        
        entrada.close();
    }
}