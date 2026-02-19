public class HelloWordExercises {

    public static void main(String[] args) {

        //imprimir un mensaje que diga tu nombre en lugar de ¡hola mundo!
        System.out.println("¡Briyit Rodriguez!"); // imprime el nombre

        //imprime dos lineas; "hola" y luego "mundo " con un solo println

        String greet = "Hola"; // variables
        String word = "world";

        System.out.println(greet  + "\n" +  word); // las escribimos con salto de lineaDebugging

        // alade un comentario de lo que hace cada linea del programabeyond

        // crea un comentario en varioas lineas

        /* la practica hace al maestro
        madie es genio porqie si , no nacio se hizo
         */

        // imprime tu edad , tu color favorito y tu ciudad

        int age = 24;    //creo las variables
        String favoriteColor = "light Blue ";
        String city = "Castellon";

        System.out.println( age + favoriteColor + city );
        // Escribe una frase usando varios printl
        String wordOne="Every day,";
        String wordTwo="I'm building myself ";
        String wordThree="my future ";
        String wordFour="and know that i get my goals.";

        System.out.println( wordOne );
        System.out.println( wordTwo );
        System.out.println( wordThree);
        System.out.println( wordFour );

        //Utiliza el sistema ASCII para imprimir un diseño

        char eyes = (char) 61;
        char mouth = (char) 68;

        String face = "" + eyes+ mouth;

        System.out.println(face);

        //ejecutar el programa sin main el sistema esta esperando el identificador

        // una falta de coincidencia entre el nombre de la clase pública y el nombre del archivo fuente.
        //si se cambia el nombre de la clase por otro
    }
}
