import java.util.Scanner;

public class ss13_methods {
    public static void getRequirements()
    {
        System.out.println();
        System.out.println("Sphere Volume Program\n");
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program calculates sphere volume in liquid U.S. gallons from user-entered diameter values in inches \nand rounds to two decimal places.");
        System.out.println("Must use Java\'s *built-in* PI and pow() capabilities.");
        System.out.println("Program checks for non-integers and non-numeric values.");
        System.out.println("Program continues to prompt user entry until no longer requested, prompt accepts upper and lower case letters.");
        System.out.println();
    }

    public static void getVolume()
    {
        int diameter = 0;
        double volume = 0.0;
        double gallons = 0.0;
        char choice = ' '; //initialize to space character
        Scanner sc = new Scanner(System.in);

        do
        {
            System.out.print("Please enter diameter in inches: ");
            while (!sc.hasNextInt())
             {
                System.out.println("Not valid integer!\n");
                sc.next();
                System.out.print("Please try again. Enter Diameter in inches: ");
             }
           diameter = sc.nextInt();
           
           System.out.println();

           volume = ((4.0/3.0) * Math.PI * Math.pow(diameter/2.0, 3));
           gallons = volume/231;
           System.out.println("Sphere volume: " + String.format("%,.2f", gallons) + " liquid U.S. gallons");

           System.out.print("\nDo you want to calculate another sphere volume (y or n)? ");
           choice = sc.next().charAt(0);
           choice = Character.toLowerCase(choice);
        }
        while (choice == 'y');
        System.out.println("\nThank you for using our Sphere Volume Calculator!");
    }
}
