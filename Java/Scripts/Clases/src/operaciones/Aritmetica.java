package operaciones;

public class Aritmetica{

    int a;
    int b;

    // Constructor vacio
    public Aritmetica() {
        System.out.println("Se crea el objeto por medio del contructor vacio");
    }

    // Constructor con parametros
    public Aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
    }

    // Suma el valor de las variables declaraadas como atributos
    public void sumar() { 
        a = 1;
        b = 2;
        System.out.println("El resultado de a + b es: " + (a + b));
    }

    // Suma y retorna el resultado de las variables declaradas como atributos
    public int sumarConRetorno() {
        return (a + b);
    }

    // Suma y retorna el resultado de los valores pasados como parametros
    public int sumarConParametros(int a, int b) {
        // this hace referencia el cual esta llamando al atributo o metodo de la clase 
        this.a = a;
        this.b = b;
        return sumarConRetorno();
    }   
}