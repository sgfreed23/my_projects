import java.util.Scanner;

public class ss11_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program determines whether user-entered value is alpha, numeric, or special character.");
        System.out.println("Note: Program does *not* check for non-numeric characters.");
        System.out.println("\nReferences:\n"
                        + "ASCII Background: https://en.wikipedia.org/wiki/ASCII\n"
                        + "ASCII Character Table: https://www.ascii-code.com\n"
                        + "Lookup Tables: https://www.lookuptables.com/");
        System.out.println();
    }

    public static void evaluateChar()
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter character: ");
        char ch = sc.next().charAt(0);

        if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
        {
            System.out.println(ch + " is alpha. ASCII value: " + (int)ch); 
        }
        else if (ch >= '0' && ch <= '9')
        {
            System.out.println(ch + " is numeric. ASCII value: " + (int)ch);
        }
        else
        {
            System.out.println(ch + " is special character. ASCII value: " + (int)ch);
        }
    }
}
