package src;
/*
Name conversion
Pascal name con -> usually used in class -> AddTwoNumber
Camel case name con -> usually used in function -> addTwoNumber
*/

/*package com.company; //use to group similar classes. different company ko
code cha vaneyy package le differ banauney package company ko naam
*/

//String
/*import java.util.Scanner;
public class src.Basic {
    public static void main(String[] args){
        String name = "Harry";
        System.out.print("The name is: ");
        System.out.println(name);
        System.out.println("The name is: ");
        System.out.println(name);
        Scanner scan = new Scanner(System.in);
        String na = scan.next();// read only first words
        System.out.println(na);
        Scanner sca = new Scanner(System.in);
        String nam = sca.nextLine(); //use to take all enter words
        System.out.println(nam);
    }}*/

//String method
/*public class src.Basic {
    public static void main(String[] args) {
        String name = "PrashanNa";
        String lstring = name.toLowerCase(); //Print lowercase
        System.out.println(lstring);

        int value = name.length();
        System.out.println(value);
        System.out.println(name.substring(1,8));
        System.out.println(name.replace('N','n'));
    }
}*/

//Array
/*public class src.Basic {
    public static void main(String[] args) {
        //int[] marks = new int[5];  //Declaration + Memory allocation
        int mark[]= {100,20,15,2,2,5,8,69,96,54};
        String students[] = {"Sus", "Pras", "Hus"};
        System.out.println(mark.length);

        //Using for loop for array
        for (int i=0;i<mark.length;i++){
            System.out.println(mark[i]);
        }

        //Reverse
        for (int i= mark.length - 1;i>=0;i--){ //-1 becoz array ma 0 dekhi count huncha
            System.out.println(mark[i]);
        }

        //Using for-each loop
        for(int element: mark){
            System.out.println(element);
        }
    }
}*/

//Multidimensional Array -> Arrays of arrays
/*public class src.Basic {
    public static void main(String[] args) {
        int flats[][] = new int[2][3];
        flats[0][0] = 101;
        flats[0][1] = 102;
        flats[0][2] = 103;
        flats[1][0] = 201;
        flats[1][1] = 202;
        flats[1][2] = 203;

        System.out.println("Printing 2-D array");
        for (int i =0;i< flats.length; i++){
            for (int j =0; j<flats[i].length;j++){
                System.out.print(flats[i][j]);
                System.out.print(" ");
            }
            System.out.println(" ");
        }
    }
}*/

//Method -> function inside the class
/* public class src.Basic {
    static int logic(int x, int y) {  //static lekhyo vaney it is shared by all
        //Without static sabai obj ko separate copy huncha so class bata obj create garnu parcha
        //Without static->  int logic(int x, int y) {
        int z;
        if(x>y){
            z = x+y;
        }
        else{
            z = (x+y)*5;
        }
        return z;
    }

    public static void main(String[] args) {
        int a = 5, b = 7, c;
         // Without static obj create
        //src.Basic obj = new src.Basic();
        //c = obj.logic(a, b);
        c = logic(a , b);
        System.out.println(c);
    }
} */
//In case of array reference is passed
/*public class src.Basic {
    static void change(int[] arr){
        arr[0]= 69;
    }

    public static void main(String[] args) {
        int[] marks = {100, 95, 65, 25, 2};
        change(marks);
        System.out.println("The value is: " + marks[0]);

    }
}*/

//Varargs
/*
public class src.Basic {
    static int sum(int ...arr) {//jati ota argument pani lincha

        int result = 0;
       for (int a: arr){
           result += a;
       }
       return result;
    }

    public static void main(String[] args) {
        System.out.println("The sum of 4 and 5 is:" + sum(4, 5));
        System.out.println("The sum is:" + sum(69, 4, 5));
        System.out.println("The sum is:" + sum(3,8,4, 5));
    }
}*/

//Recursion
public class Basic {
    static int factorial(int n){
        if(n ==0 || n ==1){
            return 1;
        }
        else{
            return n * factorial(n-1);
        }
    }

    public static void main(String[] args) {
        int x = 4;
        System.out.println("The value is: " + factorial(x));
    }
}