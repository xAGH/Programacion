package Ciclos;

public class BreakContinue {

    public static void main(String[] args) {
        // Break Permite romper un ciclo, es decir, terminarlo
        for (int i = 0; i < 10; i++) {
            if (i == 5) {
                break;
            }
            System.out.println(i);
        }

        // Continue detiene el ciclo y empieza de nuevo con la siguiente iteracion
        for (int j = 0; j < 10; j++) {
            if (j % 2 != 0) {
                continue;
            }
            System.out.println(j);
        }

        // Las etiquetas o labels son partes de codigo que indican a un continue o a un break
        // a que parte del codigo deberian de ir para cumplir su funcion

        for (int x = 0; x < 10; x++) {
            etiqueta:
            if (x == 5) {
                break etiqueta; // Llamando la etiqueta en esta posicion, el break no se cumpliria, ya que la etiqueta regresa 
                                // Dentro del ciclo.
            }
            System.out.println(x);
        }

        etiqueta2:
        for (int y = 0; y < 10; y++) {
            if (y == 5) {
                continue etiqueta2; // En este caso, la etiqeuta hace la misma funcion que el ciclo comunmente.
            }
            System.out.println(y);
        }
    }
}
