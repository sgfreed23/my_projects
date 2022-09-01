import java.util.*;

public class ss6_methods {
    public static void getRequirements(){
        
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program prompts user for first name and age, then prints results.");
        System.out.println("Create four methods from the following requirements");
        System.out.println("1) getRequirements(): Void method displays program requirements.");
        System.out.println("2) getUserInput(): Void Method Prompts for user input,");
        System.out.println("    then calls two methods: myVoidMethod() and myValueReturningMethod().");
        System.out.println("3) myVoidMethod():");
        System.out.println("    a. Accepts two arguments: String and int");
        System.out.println("    b. Prints user's first name and age.");
        System.out.println("4) myValueReturningMethod():");
        System.out.println("    a. Accepts two arguments: String and int.");
        System.out.println("    b. Returns Strign contianing first name and age.");

    }

    public static void getUserInput(){
        System.out.print("Enter first name: ");
        Scanner sc = new Scanner(System.in);
        String myName = sc.nextLine();
        System.out.print("Enter age: ");
        int myAge = sc.nextInt();

        myVoidMethod(myName, myAge);
        System.out.println("value-returning method call: " + myValueReturningMethod(myName, myAge));
    }

    public static void myVoidMethod(String myName, int myAge){
        System.out.println("void method call: " + myName + " is " + myAge);
    }

    public static String myValueReturningMethod(String myName, int myAge){
        String output = myName + " is " + myAge;
        return(output);
    }
}
