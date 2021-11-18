
public class Concatenacion {

    public static void main(String[] args) {
        var usuario = "Juan";
        var titulo = "Ingeniero";

        var union = titulo + " " + usuario;
        System.out.println("Unión: " + union);
        
        var i = 3;
        var j = 4;
        
        System.out.println(i + j); // Se realiza la suma de números.
        System.out.println(i + j + usuario); // Evaluación de izquierda a derecha, realiza suma.
        System.out.println(usuario + i + j); // Contexto cadena, todo es una cadena.
        System.out.println(usuario + (i + j)); // El uso de paréntesis modifica la prioridad de lectura.
    }
}
