public class OperatorsExercises {

    public static void main ( String [] args){

        // 1.crea una variable con el resultado de cada operacion aritmetica

        int suma= 12+20;
        int resta= 12-20;
        int division= 12/20;
        int modulo = 12 % 20;
        int multiplicacion= 12*20;

        System.out.println(suma);
        System.out.println(resta);
        System.out.println(multiplicacion);
        System.out.println(division);
        System.out.println(modulo);

        // 2. crea una variable para cada tipo de asignacion

        int a = 9;
        System.out.println("a es ="+ a);
        int b = 19;

        a +=3;
        System.out.println("ahora a es ="+ a);

        a -=3;
        System.out.println("ahora a es ="+ a);

        a /=3;
        System.out.println("ahora a es ="+ a);

        a %=3;
        System.out.println("ahora a es ="+ a);

        // imprime 3 comparaciones verdaderas con diferentes operadores de comparacion

        System.out.println(5+3 == 5+3);
        System.out.println(5>3 == 5<10);
        System.out.println(5+3 != 5+10);

        // imprime 3 falsas

        System.out.println(5+9 == 5+3);
        System.out.println(5>3 == 20<10);
        System.out.println(5+3 != 5+3);

        // operador logico and

        System.out.println(5>3 && 8<9);


        // operador logico or

        System.out.println( 3>1 || 9<3);

        // combina ambos operadores logicos

        System.out.println((5> 3 && 8<10) || 2 ==2);

        // añade alguna negacion
        System.out.println(!(9 == b));

        // 3 ejemplos de operadores unitarios

        int c = 20;
        System.out.println(c);

        c += 200;
        System.out.println(c);

        System.out.println(+c);
        System.out.println(--c);
        System.out.println(++c);
        System.out.println(c++);
        System.out.println(c);

        // combina operadores aritmeticos , de comparacion y logicos

        System.out.println(((20+10)== 30) || 2<3 == 10>2 );


        String  name = "Briyit ";

        System.out.println(name.length());// longitud

        // obtener caracter

        System.out.println(name.charAt(0));// remember the first is 0

        //subcadena

        System.out.println(name.substring(2));
        System.out.println(name.substring(1 , 3));

        //uppercae or lowcase
        System.out.println(name.toLowerCase());
        System.out.println(name.toUpperCase());

        // investigar como funciona cada una
        // contains

        System.out.println("hello , briyit".contains("iyi") );

        // comparacion

        System.out.println(name. equals("BRIYIT"));
        System.out.println(name. equalsIgnoreCase("briyit "));


       // equas  buena practica no ==

        // trim

        System.out.println("Hola me llamo briyit");

        System.out.println("Hola me llamo briyit".trim());

        //replace

        System.out.println("Hola me llamo briyit".replace(" " , ""));
        System.out.println("Hola me llamo briyit".replace("briyit" , "Liset"));

        // format

        var age= 37;
        System.out.println(String.format("Hola , Usuario. Tengo 24 años.",name, age ));// sitios concretos
        System.out.println(String.format("Hola , %s. Tengo  %d.",name, age ));// sitios concretos %s para string , %d numeros enteros. f para desimales




    }
}
