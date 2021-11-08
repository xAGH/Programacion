package operaciones;

public class PruebaAritmetica{

    public static void main(String[] args) {
        
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.sumar();
        aritmetica1.a = 10;
        aritmetica1.b = 5;
        System.out.println("Resultado con retorno:" + (aritmetica1.sumarConRetorno()));
        System.out.println("Resultado con parametros: " + (aritmetica1.sumarConParametros(19, 1)));

        // Se crea el objeto llamando al constructor que recibe como parametros los dos numeros.
        Aritmetica aritmetica2 = new Aritmetica(10, 4);
        System.out.println("Resultado con constructor: " + (aritmetica2.sumarConRetorno()));
    }
}