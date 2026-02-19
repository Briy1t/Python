public class StringExercises {

    public static void main (String [] args) {

        // Concatena dos cadenas de texto.

        String greet = "Hola";
        String question = "How are you?";
        System.out.println(greet+ ", "+ question);

        // Muestra la longitud de una cadena de texto
        System.out.println(question.length());

        // Muestra el primer y ultimo caracter de un string

        System.out.println(greet.charAt(0));
        System.out.println(greet.charAt(greet.length()-1));

        // Combierte a mayusculas y minusculas un string

            System.out.println(greet.toLowerCase());
            System.out.println(greet.toUpperCase());//

        // Comprueba si una cadena de texto tiene una palabra

        System.out.println("Hola a todos, ¿como estan?".contains("como"));

        // Fomarmate un String con un entero

        int pounts = 20;
        String user = "Camilo";

        System.out.println(String.format("Hola %s , su score es de: %d",user,pounts));

        // Elimina los espacios del inicio y del final

        System.out.println(" Cada dia mas cerca de cumplir la meta ".trim());

        // Sustituye todos los espacios en blanco de u string por un un guion

        System.out.println(" Cada dia mas cerca de cumplir la meta ".replace(" ", "-"));

        // Comprueba si dos String son iguales


        String user1 = "Sara";

        System.out.println(user1.equalsIgnoreCase("SARA"));


        // Comprueba si dos string tienen la misma longitud

        int len = user.length();
        int len1 = user1.length();

        System.out.println(len == len1);

        // Condicionales

        // senteica if

        var age = 3;

        System.out.println("Edad del usuario" + age );

        if (age >= 18 ){
            System.out.println("El usuario es mayor de edad");
        } else {
            System.out.println("El usuario es menor de edad");
        }
    }

}
