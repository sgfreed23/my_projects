import java.util.Scanner;

public class ss12_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed");
        System.out.println("Temperature Conversion Program\n");
        System.out.println("Program converts user-entered temperatures into Fahrenheit or Celcius scales.");
        System.out.println("Program continues to prompt for user entry until no longer requested.");
        System.out.println("Note: upper or lower case letters permitted. Though, incorrect entries are not permitted.");
        System.out.println("Note: Program does not validate numeric data.");
        System.out.println();
    }

    public static void convertTemp()
    {
        Scanner sc = new Scanner(System.in);
        double temperature = 0.0;
        char choice;
        char type;

        do
        {
            System.out.print("Fahrenheit to Celcius? Type \"f\" or Celcius to Fahrenheit? \"c\": ");
            type = sc.next().charAt(0);
            type = Character.toLowerCase(type);
            if(type == 'f')
            {
                System.out.print("Enter temperature in Fahrenheit: ");
                temperature = sc.nextDouble();
                temperature = ((temperature - 32)*5)/9;
                System.out.println("Temperature in Celius = " + temperature);
            }
            else if (type == 'c')
            {
                System.out.print("Enter temperature in Celius: ");
                temperature = sc.nextDouble();
                temperature = (temperature * 9/5) +32;
                System.out.println("Temperature in Fahrenheit = " + temperature);
            }
            else
            {
                System.out.println("Incorrect entry. Please try again.");
            }

            System.out.print("\nDo you want to convert a temperature (y or n)?");
            choice = sc.next().charAt(0);
            choice = Character.toLowerCase(choice);
        }
        while (choice == 'y');

        System.out.println("\nThank you for using our Temperature Conversion Program!");
    }
}
