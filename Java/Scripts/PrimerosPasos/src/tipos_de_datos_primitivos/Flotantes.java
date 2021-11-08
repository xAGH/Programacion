package TiposDeDatosPrimitivos;

public class Flotantes {

    public static void main(String[] args) {
        /*
            Tipos primitivos flotantes: float(32 bits), double(64 bits)
        */
        float numeroFloat = (float) 3.4028235E38D;
        System.out.println("Valor mínimo del float: " + Float.MIN_VALUE);
        System.out.println("Valor máximo del float: " + Float.MAX_VALUE);
        System.out.println("Valor del flotante = " + numeroFloat);
        
        double numeroDouble = 1.7976931348623157E308;
        System.out.println("Valor mínimo del double: " + Double.MIN_VALUE);
        System.out.println("Valor máximo del double: " + Double.MAX_VALUE);
        System.out.println("Valor del doble = " + numeroDouble);
    }
}
