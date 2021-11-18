package clases;

public class PruebaPersona {
    
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Alejo";
        persona1.apellido = "Giraldo";
        persona1.desplegarInformacion();

        Persona persona2 = new Persona();
        persona2.nombre = "Michael";
        persona2.apellido = "Giraldo";
        persona1.desplegarInformacion();

    }
}
