public class OperadoresIncrementoDescremento {
    
    public static void main(String[] args){

        int x = 5, y;

        x++; //x = x + 1
        System.out.println(x);

        x--; //x = x - 1
        System.out.println(x);

        // En este caso estamos asignando el valor de x a y y despues le estamos sumando 1 a x, por lo tanto
        // en este caso la y es igual a 5 y despues x es igual a 6.
        y = x++;
        System.out.println(y);
        System.out.println(x);

        // En este caso estamos aumentando el valor de x en uno y despues le asignamos ese valor a y.
        y = ++x;
    }
}
