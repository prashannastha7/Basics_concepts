package src;
/*class Employee{
    int id;
    String name;
    public void printDetails(){
        System.out.print("My name is "+ name ) ;
        System.out.println("& Id is: " + id);
    }
}
public class OOP {
    public static void main(String[] args) {
        Employee ram = new Employee(); //Obj creation
        ram.id = 69;
        ram.name= "RAM";

        //Printing the details
        //System.out.println(ram.name);
        //System.out.println(ram.id);
        ram.printDetails();
    }
}*/

//Private access
/*class Myemployee{
    private int id;
    private String name;

    public String getName(){
        return name;
    }

    public void setName(String n){
        name = n;
    }
    public void setId(int i){
        id = i;
    }
    public int getId(){
        return id;
    }
}
public class OOP {

    public static void main(String[] args) {
        Myemployee ramu = new Myemployee();
        ramu.setName("RamuDas");
        System.out.println(ramu.getName());
    }}*/

//Constructor

/*class MainEmployee{
    private int id;
    private String name;

    public MainEmployee(){ //Constructor
        id = 69;
        name = "Prashanna";
//           OR
//        public MainEmployee(myName){ //Constructor
//            id = 69;
//            name = myName;
    }
    public String getName(){
        return name;
    }

    public void setName(String n){
        name = n;
    }
    public void setId(int i){
        id = i;
    }
    public int getId() {
        return id;
    }
}

public class OOP {
    public static void main(String[] args) {
        MainEmployee e = new MainEmployee(); //to pass argument new main..("Prashanna")
        System.out.println(e.getName());
    }
}*/

//Inheritance
/*//The final Keyword
//If you don't want other classes to inherit from a class,
// use the final keyword:
// final class Base{}
class Base{
    int x;

    public int getX() {
        return x;
    }

    public void setX(int x) {
        System.out.println("I am setting x now");
        this.x = x;
    }
    public void Base(){
        System.out.println("I am constructor.");
    }
}

class Derived extends Base{

}
public class OOP {
    public static void main(String[] args) {
        Derived d = new Derived();
        d.setX(4);
        System.out.println(d.getX());

    }
}
*/

//Constructor in Inheritance
/*class Base {
    Base() {
        System.out.println("Hello I am Constructor..");
    }

    Base(int a) { //Overloading
        System.out.println("I am an Overconstructor with value: " + a);

    }
}
class Derived extends Base{

    Derived(){
       // super(0); // to called another base with argument
        System.out.println("Derived constructor.");
    }
    Derived(int x, int y){
        super(x); //argument ma x pass garna mathi base class ma
        System.out.println("Overloaded Derived constructor.");

    }
}

public class OOP {
    public static void main(String[] args) {
       // Base b = new Base();
        //Derived d = new Derived(); //First base class ko constructor run huncha aani derived ko
        Derived d = new Derived(14,69); // to called argument derived
    }
}*/

//Method overriding
/*//overloading same class ma duita same name method
//overriding ma diff class same name method
class A{
    public int meth1(){
        return 4;
    }

    public void meth2(){
        System.out.println("I am method 2 of class A");
    }
}

class B extends A{
    public void meth2(){ //Overriding
        System.out.println("I am method 2 of class B");
    }
    public void meth3(){
        System.out.println("I am method 3 of class B");
    }
}

public class OOP {
    public static void main(String[] args) {
        A a = new A();
        a.meth2();

        B b = new B();
        b.meth2();

    }
}*/

//Dynamic Method Dispatch
/*
class Base{
void meth1()
void meth2()}
Class derived extends Base{
void meth2()
void meth3()}
main()
Base obj = new Derived();
obj.meth1() milcha allowed
obj.meth2() allowed it called derived class wala meth2
obj.meth3() not allowed because base class ma chaina
*/

//Abstract Class
/*abstract class Parent{
    public Parent(){
        System.out.println("I am constructor of base");
    }
    public void hello(){
        System.out.println("Hello");
    }
    abstract public void greet();
}

class Child extends Parent{
    @Override
    public void greet() {
        System.out.println("Good morning");

    }
}

//class Childs extends Parent{ } //error becoz ki abstract banauna parcha ki ta greet overiding hannu parcha
abstract class Childs extends Parent{
    public void th(){
        System.out.println("I am learning");
    }
}

public class OOP {
    public static void main(String[] args) {
        Child c = new Child();
        //Parent p = new Parent();//abstract ko obj banauna mildaina
    }
}*/

//Interfaces:Is a completely "abstract class" that is used to group related methods with empty bodies
//implement garda interfaces ma vako sabai laii garnaiii parcha
/*interface Animal {
    int a = 45;
    public void animalSound(); // interface method (does not have a body)
    public void sleep(); // interface method (does not have a body)
}

// Pig "implements" the Animal interface
class Pig implements Animal {
    public void animalSound() {
        // The body of animalSound() is provided here
        System.out.println("The pig says: wee wee");
    }
    public void sleep() {
        // The body of sleep() is provided here
        System.out.println("Zzz");
    }
}

class OOP {
    public static void main(String[] args) {
        Pig myPig = new Pig();  // Create a Pig object
        myPig.animalSound();
        myPig.sleep();
        myPig.a = 69; garna mildaina becoz interface ma modify garna mildaina final huncha
    }
}*/

//Multiple interfaces in allowed
/*interface FirstInterface {
    public void myMethod(); // interface method
}

interface SecondInterface {
    public void myOtherMethod(); // interface method
}

class DemoClass implements FirstInterface, SecondInterface {
    public void myMethod() {
        System.out.println("Some text..");
    }
    public void myOtherMethod() {
        System.out.println("Some other text...");
    }
}

class OOP{
    public static void main(String[] args) {
        DemoClass myObj = new DemoClass();
        myObj.myMethod();
        myObj.myOtherMethod();
    }
}*/

//Interfaces and class
/*interface MyCamera{
    void takeSnap();
    void recordVideo();
    private void greet(){
        System.out.println("Good Morning");
    }
    default void record4KVideo(){ //default banayo vaney implement ma add garnu pardaina
        greet();
        System.out.println("Recording in 4k...");
    }
}
interface MyWifi{
    String[] getNetworks();
    void connectToNetwork(String network);
}

class MyCellPhone{
    void callNumber(int phoneNumber){
        System.out.println("Calling "+ phoneNumber);
    }
    void pickCall(){
        System.out.println("Connecting... ");
    }

}

class MySmartPhone extends MyCellPhone implements MyWifi, MyCamera{
    public void takeSnap(){
        System.out.println("Taking snap");
    }
    public void recordVideo(){
        System.out.println("Taking snap");
    }
    //    public void record4KVideo(){
//        System.out.println("Taking snap and recoding in 4k");
//    }
    public String[] getNetworks(){
        System.out.println("Getting List of Networks");
        String[] networkList = {"Harry", "Prashanth", "Anjali5G"};
        return networkList;
    }
    public void connectToNetwork(String network){
        System.out.println("Connecting to " + network);
    }
}
public class OOP {
    public static void main(String[] args) {
        MySmartPhone ms = new MySmartPhone();
        ms.record4KVideo();
        // ms.greet(); --> Throws an error!
        String[] ar = ms.getNetworks();
        for (String item: ar) {
            System.out.println(item);
        }
    }
}*/

//Default
/*interface Animal{
    // Default method
    default void say(){
        System.out.println("Hello, this is default method");
    }
    // Abstract method
    void bark();
}
public class OOP implements Animal{

    @Override
    public void bark() {
        System.out.println("Dog barks!");
    }
    public static void main(String[] args) {
        CWH obj1 = new CWH();
        obj1.bark();
        obj1.say();
    }
}*/

//class child extends interface -> mildaina inheritance garna midlaina yesari
//interface child extends interface -> milcha
//abstract child implements interface -> milcha abstract parent vako bela

//Inheritance in interfaces
/*
interface sample{
    void meth1();
    void meth2();
}

interface childsample extends sample{
    void meth3();
    void meth4();
}

class Mysample implements childsample{
    public void meth1(){
        System.out.println("meth1");
    }
    public void meth2(){
        System.out.println("meth2");
    }
    public void meth3(){
        System.out.println("meth3");
    }
    public void meth4(){
        System.out.println("meth4");
    }
}

public class OOP {
    public static void main(String[] args) {
        Mysample obj = new Mysample();
        obj.meth1();
        obj.meth2();
    }
}*/

//polymorphism
/*class Animal {
    public void animalSound() {
        System.out.println("The animal makes a sound");
    }
}

class Pig extends Animal {
    public void animalSound() {
        System.out.println("The pig says: wee wee");
    }
}

class Dog extends Animal {
    public void animalSound() {
        System.out.println("The dog says: bow wow");
    }
}

class OOP {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();  // Create a Animal object
        Animal myPig = new Pig();  // Create a Pig object
        Animal myDog = new Dog();  // Create a Dog object
        myAnimal.animalSound();
        myPig.animalSound();
        myDog.animalSound();
    }
}*/

//Polymorphism in interfaces
/*
interface MyCamera2{
    void takeSnap();
    void recordVideo();
    private void greet(){
        System.out.println("Good Morning");
    }
    default void record4KVideo(){
        greet();
        System.out.println("Recording in 4k...");
    }

interface MyWifi2{
    String[] getNetworks();
    void connectToNetwork(String network);
}

class MyCellPhone2{
    void callNumber(int phoneNumber){
        System.out.println("Calling "+ phoneNumber);
    }
    void pickCall(){
        System.out.println("Connecting... ");
    }

}

class MySmartPhone2 extends MyCellPhone2 implements MyWifi2, MyCamera2{
    public void takeSnap(){
        System.out.println("Taking snap");
    }
    public void recordVideo(){
        System.out.println("Taking snap");
    }
    //    public void record4KVideo(){
//        System.out.println("Taking snap and recoding in 4k");
//    }
    public String[] getNetworks(){
        System.out.println("Getting List of Networks");
        String[] networkList = {"Harry", "Prashanth", "Anjali5G"};
        return networkList;
    }
    public void connectToNetwork(String network){
        System.out.println("Connecting to " + network);
    }
    public void sampleMeth(){
        System.out.println("meth");
    }
}
public class OOP {
    public static void main(String[] args) {
        MyCamera2 cam1 = new MySmartPhone2(); // This is a smartphone but, use it as a camera
        // cam1.getNetworks(); --> Not allowed
        // cam1.sampleMeth(); --> Not allowed

        cam1.record4KVideo();

        MySmartPhone2 s = new MySmartPhone2();
        s.sampleMeth();
        s.recordVideo();
        s.getNetworks();
        s.callNumber(7979);
    }}*/

