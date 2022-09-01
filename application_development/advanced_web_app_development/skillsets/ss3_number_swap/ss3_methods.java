import java.util.Scanner;

public class ss3_methods {
    public static void getRequirements(){
        
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program Requirements: ");
        System.out.println("1. Program swaps two user-entered floating-point values");
        System.out.println("2. Create at least two user-defined methods: getRequirements() and numberSwap()");
        System.out.println("3. Must perform data validation: numbers must be floats");
        System.out.println("4. Print numbers before/after swapping");
        System.out.println();

    }

    public static void numberSwap(){
        float x = 0;
        Scanner num1 = new Scanner(System.in);
        System.out.print("Enter num1: ");
        while (!num1.hasNextFloat()) {
            System.out.println("Invalid Input!");
            num1.next();
            System.out.println();
            System.out.print("Please try again. Enter num1: ");
        }
        x = num1.nextFloat();

        System.out.println();

        float y = 0;
        Scanner num2 = new Scanner(System.in);
        System.out.print("Enter num2: ");
        while (!num2.hasNextFloat()) {
            System.out.println("Invalid Input!");
            num2.next();
            System.out.println();
            System.out.print("Please try again. Enter num2: ");
        }
        y = num2.nextFloat();

        System.out.println();
        System.out.println("Before Swap: ");
        System.out.println("num1 = " + x);
        System.out.println("num2 = " + y);
        System.out.println();

        float z = 0;
        z = x;
        x = y;
        y = z;

        System.out.println("After Swap: ");
        System.out.println("num1 " + x);
        System.out.println("num2 " + y);
        System.out.println();

    } 
}
