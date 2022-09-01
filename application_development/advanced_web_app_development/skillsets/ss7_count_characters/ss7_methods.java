import java.util.*;

public class ss7_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed\n");
        System.out.println("Program Requirements:");
        System.out.println("\t1. Counts number and types of characters from user-entered string.");
        System.out.println("\t2. Count: total, letters (upper-/lower-case), numbers, spaces, and other characters.");
        System.out.println("\tHint: Helpful methods: isLetter(), isDigit(), isSpaceChar(), and other.");
        System.out.println();
    }
    public static void countChar()
      {
        int letter = 0;
        int space = 0;
        int num = 0;
        int upper = 0;
        int lower = 0;
        int other = 0;
        String input = "";
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter string: ");
        input = sc.nextLine();

        char[] ch = input.toCharArray();

        for(int i = 0; i < input.length(); i++)
          {
            if(Character.isLetter(ch[i]))
              {
                if(Character.isUpperCase(ch[i]))
                  {
                    upper++;
                  }
                if(Character.isLowerCase(ch[i]))
                {
                  lower++;
                }
              letter++;
              }
            else if(Character.isDigit(ch[i]))
            {
              num++;
            }
            else if(Character.isSpaceChar(ch[i]))
            {
              space++;
            }
            else
            {
              other++;
            }
          }



        System.out.println("\nYour string: \"" + input + "\" has the following number and types of characters:");
        System.out.println("Total number of characters: " + input.length());
        System.out.println("Letter(s): " + letter);
        System.out.println("Upper-case letter(s): " + upper);
        System.out.println("Lower-case letter(s): " + lower);
        System.out.println("Number(s): " + num);
        System.out.println("Space(s): " + space);
        System.out.println("Other character(s): " + other);
        sc.close();
      }
}
