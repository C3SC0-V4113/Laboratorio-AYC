
//Importamos paquete para poder trabajar con expresiones regulares
import java.util.regex.Matcher;
//Importamos paquete para trabajar con un patrón
import java.util.regex.Pattern;

/**
 * @author cesco_valle
 */
public class Ejercicio2 {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String patron = ("(while|if|else|do|for|foreach|bool|int|double|char|string)|([a-zA-Z]+)|([>|<|=|+]+)|([0-9]+)|([(|)]+)|([{|}])|(;)|([\\[|\\]])");
        // La expresión que vamos a evaluar es la siguiente:
        String texto = "x=1; do{ if (w==1) { While(x<5) { z++; } } else{ Array[i] = 7; } }while(j==0); int no=5; double des=3.5;bool flag=true; char knife='a'; string='space_jam';for (int i = 0; i < 5; i++) {i;};String[] cars = {'Volvo', 'BMW', 'Ford', 'Mazda'};for (String i : cars) {i;}";

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

            String tokenTipo8 = matcher.group(8);
            if (tokenTipo8 != null) {
                System.out.println("Corchetes: " + tokenTipo8);
            }
        }
    }
}
