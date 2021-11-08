package TiposDeDatosPrimitivos;

public class Caracter {

    public static void main(String[] args) {
        char miCaracter = 'a';
        System.out.println("miCaracter = " + miCaracter);

        char varChar = '\u0021'; // Se indica un valor unicode
        System.out.println("varChar = " + varChar);

        char varCharDecimal = 33; // Se indica un valor unicode decimal
        System.out.println("varCharDecimal = " + varCharDecimal);

        char varCharSimbolo = '!';
        System.out.println("varCharSimboplo = " + varCharSimbolo);

        var varChar2 = '\u0021'; // Se indica un valor unicode, por lo cual es tomado como tipo de dato char.
        System.out.println("varChar2 = " + varChar2);

        var varCharDecimal2 = (char) 33; // Se indica un valor unicode decimal, sin embarego, debido al iteral del var, es tomado como int.
        System.out.println("varCharDecimal2 = " + varCharDecimal2);

        var varCharSimbolo2 = '!'; // Es tomado como char
        System.out.println("varCharSimbolo2 = " + varCharSimbolo2);

        int variableEnteraSimbolo = '!'; // Al asignar un char a una variable int, se guarda el valor Unicode decimal.
        System.out.println("variableEnteraSimbolo = " + variableEnteraSimbolo);
    }
}
