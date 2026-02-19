public class VariablesAndConstantsExercises {

    public static void main (String[] args){

        // 1. Declara una variable de tipo string y asignale tu nombre

        String name = "Briyit ";

        //2. Crea una variable de tipo int y asignale tu edad

        int age = 24;

        //3. double y asignale tu estatura

        double altura= 1.70;

        //4. boolean que te indique que si te gusta programas

        boolean meGustaProgramar = true;

        //%. constante con el gmail

        final String gmail = "Lisetrodriguezastros@gmail.com";

        //6. char y guarda tu inicial

        char inicial =  'l' ;

        //7. tipo string con tu localidad y cambiala y vuelve a imprimirla

        String localidad = "Nules";

        System.out.println(localidad);

        localidad = "Castellon";

        System.out.println(localidad);

        //8. int llamada a y otra b , e imprime la suma

        int a = 100;
        int b = 300;

        System.out.println(a+b);

        //9. iniciar una varible y luego imprimirla antes de imprimirla darle un valor

        String variable = "";

        variable = "It's enough for today ";
        System.out.println(variable);



        // el modulo de python //

        // Asignacion =

        a = 3;
        b = 20;
        System.out.println(a+b);

        a = b;
        System.out.println(a);

        a += 1 ; // = a = a + 1  igual con los otros
        System.out.println(a);

        a %= 2 ; // = a = a + 1  igual con los otros
        System.out.println(a);

        // comparacion

        a += 1 ; // = a = a + 1  igual con los otros
        System.out.println(a == b);
        System.out.println(a != b);

        //Operadores logicos, tabla de verdad
        // && si = todas tiene que ser verdaderas para que sea verdadero

        System.out.println(true && true);
        System.out.println(true && false);

        System.out.println(3>6 && 10==10);

        // 0r || alguna verdadera para que sea verdadero

        System.out.println(true || true);
        System.out.println(false || false);
        System.out.println(true || false);

        System.out.println(3>6 || 10==10);

        // Not (NOT) !

        System.out.println(!false);
        System.out.println(!true );

        System.out.println(3>6 || !(10==10));

        // unarios en ocasiones el not tambien se considera unario

        System.out.println(+b);
        System.out.println(-b);
        System.out.println(++b);
        System.out.println(b++);
        System.out.println(b);


    }
}
