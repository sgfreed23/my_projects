import java.util.Scanner;
import java.util.Random;

public class ss7_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed");
        System.out.println("Print minimum and maximum integer values.");
        System.out.println("Program prompts user to enter desired number of pseudorandom-generated integers (min 1).");
        System.out.println("Use following loop structures: for, enhanced for, while, do...while.\n");
       
        System.out.println("Integer.MIN_VALUE = " + Integer.MIN_VALUE);
        System.out.println("Integer.MAX_VALUE = " + Integer.MAX_VALUE);
        System.out.println();
    }

    public static int[] createArray()
    {
        Scanner sc = new Scanner(System.in);
        int arraySize = 0;
        //initialize variables, create Scanner object, capture user input
        System.out.print("Enter desired number of pseudorandom-generated integers (min 1): ");
        
        while (!sc.hasNextInt())
        {
            System.out.println("Not valid integer!\n");
            sc.next();
            System.out.print("Please try again. Enter valid integer (min 1): ");
        }
        arraySize = sc.nextInt();

        while (arraySize < 1) 
        {
            System.out.print("\nNumber must be greater than 0. Please enter integer greater than 0: ");
            while (!sc.hasNextInt())
            {
                System.out.println("Number must be integer: ");
                sc.next();
                System.out.print("Please try again. Enter valid integer greater than 0: ");   
            }
            arraySize = sc.nextInt();
        }
        
        int yourArray[] = new int[arraySize];
        return yourArray;
    }


    public static void generateRandomNumbers(int[] myArray)
    {
        Random r = new Random();
        int i = 0;

        System.out.println("for loop: ");
        for (i = 0; i < myArray.length; i++)
        {
            System.out.println(r.nextInt());
        }

        System.out.println("\nEnhanced for loop: ");
        for (int n: myArray)
        {
            System.out.println(r.nextInt());
        }

        System.out.println("\nwhile loop: ");
        i = 0;
        while (i < myArray.length)
        {
            System.out.println(r.nextInt());
            i++;
        }
        
        System.out.println("\ndo...while loop: ");
        i = 0;
        do {
            System.out.println(r.nextInt());
            i++;
        } while (i < myArray.length);
    }
};
