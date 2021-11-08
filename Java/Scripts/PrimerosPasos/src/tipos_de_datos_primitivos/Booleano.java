package TiposDeDatosPrimitivos;

public class Booleano {

    public static void main(String[] args) {
        boolean varBoolean = true;
        System.out.println("varBoolean = " + varBoolean);

        var edad = 30; // Variable entera por inferencia
        var esAdulto = edad >= 18; // Variable booleana por inferencia, dada de una operacion logica.
        System.out.println("esAdulto = " + esAdulto);
    }
}
