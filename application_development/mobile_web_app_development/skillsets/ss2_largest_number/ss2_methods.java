import java.util.Scanner;

public class ss2_methods {
    public static void getRequirements(){
        
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program evaluates largest of two integers");
        System.out.println("Note: Program does *not* check for non-numeric characters or non-integer values");
        System.out.println();

    }

    public static void evaluateNumber(){

        //initialize variables, create Scanner object, capture user input
        int x = 0;
        System.out.print("Enter first integer: ");
        Scanner first = new Scanner(System.in);
        x = first.nextInt();

        int y = 0;
        System.out.print("Enter second integer: ");
        Scanner second = new Scanner(System.in);
        y = second.nextInt();

        if (x > y ){
            System.out.println(x + " is larger than " + y);
        }else if (x<y) {
            System.out.println(y + " is larger than " + x);
        }else{
            System.out.println("Integers are equal");
        }

    }
}
