package Condicionales;

public class SwitchCase {

    public static void main(String[] args) {
        var numero = 2;
        var numeroTexto = "Valor desconocido";

        switch (numero) { // Switch como regla, para ejecutar una linea de codigo
            case 1 ->
                numeroTexto = "Numero uno";

            case 2 ->
                numeroTexto = "Numero dos";

            case 3 ->
                numeroTexto = "Numero tres";

            case 4 ->
                numeroTexto = "Numero cuatro";
        }

        switch (numero) { // Switch comun
            case 1:
                numeroTexto = "Numero uno";
                break;

            case 2:
                numeroTexto = "Numero dos";
                break;

            case 3:
                numeroTexto = "Numero tres";
                break;

            case 4:
                numeroTexto = "Numero cuatro";
                break;
        }
        System.out.println("numeroTexto = " + numeroTexto);
    }
}
