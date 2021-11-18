public class Variables {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Definimos una variable
        int miVariableEntera = 10;
        System.out.println(miVariableEntera);
        miVariableEntera = 5;
        System.out.println(miVariableEntera);
        
        String miVariableCadena = "Saludos";
        System.out.println(miVariableCadena);
        
        miVariableCadena = "Adios   ";
        System.out.println(miVariableCadena);
        
        // var - Inferencia de tipos de datos en Java
        var miVariableEntera2 = 15;
        System.out.println(miVariableEntera2);
        
        var miVariableCadena2 = "Nueva Cadena";
        System.out.println(miVariableCadena2);
        
        System.out.println("miVariableCadena2 = "  + miVariableCadena2);
        
        // Valores permitidos en el nombre de nuestras variables.
        var miVariable = 1;
        var _miVariable =2;
        var $miVariable = 3;
        // var áVariable = 10; No se recomienda utilizar
        // var #miVariable = 2; No se permiten utilizar carácteres especiales
    }
    
}
