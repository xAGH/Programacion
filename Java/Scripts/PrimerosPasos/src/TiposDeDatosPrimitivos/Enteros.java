package TiposDeDatosPrimitivos;

public class Enteros {

    public static void main(String[] args) {
        /*
            Tipos primitivos enteros: byte(8 bits), short(16 bits), int(32 bits), long(64 bits)
         */
        byte numeroByte = (byte) 129;
        System.out.println("Valor mínimo del byte: " + Byte.MIN_VALUE);
        System.out.println("Valor máximo del byte: " + Byte.MAX_VALUE);
        System.out.println("Valor byte: " + numeroByte);

        short numeroShort = (short) 32768;
        System.out.println("Valor mínimo del short: " + Short.MIN_VALUE);
        System.out.println("Valor máximo del short: " + Short.MAX_VALUE);
        System.out.println("Valor short = " + numeroShort);

        int numeroInt = (int) 2147483648L;
        System.out.println("Valor mínimo del entero: " + Integer.MAX_VALUE);
        System.out.println("Valor máximo del entero: " + Integer.MIN_VALUE);
        System.out.println("Valor entero = " + numeroInt);

        long numeroLong = 9223372036854775807L;
        System.out.println("Valor mínimo del long: " + Long.MAX_VALUE);
        System.out.println("Valor máximo del long: " + Long.MIN_VALUE);
        System.out.println("Valor long = " + numeroLong);
    }
}
