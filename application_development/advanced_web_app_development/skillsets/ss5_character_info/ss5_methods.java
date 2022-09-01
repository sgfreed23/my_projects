import java.util.*;

public class ss5_methods
{
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed\n");
        System.out.println("Program Requirements:");
        System.out.println("Program determines total number of characters in line of text,\nas well as number of times specific character is used.");
        System.out.println("Program displays character's ASCII value.\n");

    }

    public static void determineChar()
    {
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter line of text: ");
      String st = sc.nextLine();
      System.out.print("Enter character you would like to check: ");

      char ch = sc.next().charAt(0);

    System.out.println("\nThe number of characters in the line of text is: " + st.length());

     int count=0;
     for(int i=0; i<st.length(); i++)
     {
         if(st.charAt(i) == ch)
         count++;
     }

   System.out.println("The character " + ch +  " appears " + count + " time(s) in line of text. " );

   if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
   {

     System.out.println("ASCII value: " + (int)ch);
   }

   else if(ch >= '0' && ch< '9')
   {
     System.out.println( "ASCII value: "+(int)ch);
   }

  else{System.out.println("ASCII value: "+(int)ch);

        }
    }
}