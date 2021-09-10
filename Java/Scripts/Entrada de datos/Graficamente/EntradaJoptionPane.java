// Se importa JOptionPane
import javax.swing.JOptionPane;

public class EntradaJoptionPane{
    public static void main(String[] args) {
        String cadena;
        int entero;
        char letra;
        double decimal;

        // Se le da un valor a las variables el cual seran los datos ingresados por teclado.
        cadena = JOptionPane.showInputDialog("Digite una cadena: ");

        // Se hace la conversion de String a entero ya que JOptionPane devuelve una string.
        entero = Integer.parseInt(JOptionPane.showInputDialog("Digite un entero: "));

        // Se toma solo la primera letra del string ingresado.
        letra = JOptionPane.showInputDialog("Digite un caracter: ").charAt(0);

        // Se hace la conversion de String a double ya que JOptionPane devuelve una string. Con JOptionPane se declara la parte decimal con un punto.
        decimal = Double.parseDouble(JOptionPane.showInputDialog("Digite un decimal: "));


        // SALIDA DE DATOS CON JOPTIONPANE
        JOptionPane.showMessageDialog(null, "La cadena es: "+cadena);
        JOptionPane.showMessageDialog(null, "El entero es: "+entero);
        JOptionPane.showMessageDialog(null, "La letra es: "+letra);
        JOptionPane.showMessageDialog(null, "El decimal es: "+decimal);
    }
}