
//Importamos paquete para poder trabajar con expresiones regulares
import java.util.regex.Matcher;
//Importamos paquete para trabajar con un patrón
import java.util.regex.Pattern;

/**
 * @author cesco_valle
 */

public class Ejemplo1 {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String patron = ("(while|if)|([a-zA-Z]+)|([>|<|=]+)|([0-9]+)|([(|)]+)|([{|}])|(;)");
        // La expresión que vamos a evaluar es la siguiente:
        String texto = "while (x=0) < (y=0) {if (x=1) {x=7}}";

        Pattern p = Pattern.compile(patron);
        Matcher matcher = p.matcher(texto);

        System.out.println("Guia 5 Análisis Léxico");
        while (matcher.find()) {
            String tokenTipo1 = matcher.group(1);
            if (tokenTipo1 != null) {
                System.out.println("Palabras reservadas: " + tokenTipo1);
            }

            String tokenTipo2 = matcher.group(2);
            if (tokenTipo2 != null) {
                System.out.println("Variables: " + tokenTipo2);
            }

            String tokenTipo3 = matcher.group(3);
            if (tokenTipo3 != null) {
                System.out.println("Operador: " + tokenTipo3);
            }

            String tokenTipo4 = matcher.group(4);
            if (tokenTipo4 != null) {
                System.out.println("Números: " + tokenTipo4);
            }

            String tokenTipo5 = matcher.group(5);
            if (tokenTipo5 != null) {
                System.out.println("Paréntesis: " + tokenTipo5);
            }

            String tokenTipo6 = matcher.group(6);
            if (tokenTipo6 != null) {
                System.out.println("Llaves: " + tokenTipo6);
            }

            String tokenTipo7 = matcher.group(7);
            if (tokenTipo7 != null) {
                System.out.println("Punto y coma: " + tokenTipo7);
            }
        }
    }
}
