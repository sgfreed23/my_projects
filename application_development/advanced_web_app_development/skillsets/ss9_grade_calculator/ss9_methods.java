import java.util.*;

public class ss9_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed\n");
        System.out.println("Program Requirements:");
        System.out.println("1. Returns letter grade, based on user-entered numeric score.");
        System.out.println("2. Program checks for non-numeric and out of range values.");
        System.out.println("Note: Program is accurate to the 6th fraction digit (i.e., 6 digits right of decimal point).");
    }
    public static void getScore()
    {
        double score = 0.0;
        Scanner sc = new Scanner(System.in);
        System.out.print("\nPlease enter grade between 0 to 100, inclusive: ");
        while(!sc.hasNextDouble())
          {
            System.out.println("Not valid number!\n");
            sc.next();
            System.out.print("Please try again. Enter grade between 0 to 100, inclusive: ");
          }
        score = sc.nextDouble();
        getGrade(score);

        sc.close();
    }

    public static void getGrade(double score)
    {
      String grade = "";

      if (score < 0 || score > 100)
        {
          System.out.print("\nOut of range!");
          getScore();
        }
      else
        {
        if (score < 60 && score >=0)
        grade = "F";

        else if (score <63 && score >=60)
        grade = "D-";
        else if (score < 67 && score >= 63)
        grade = "D";
        else if (score < 70 && score >= 67)
        grade = "D+";

        else if (score <73 && score >= 70)
        grade = "C-";
        else if (score < 77 && score >= 73)
        grade = "C";
        else if (score <80 && score >= 77)
        grade = "C+";

        else if (score < 83 && score >= 80)
        grade = "B-";
        else if (score < 87 && score >= 83)
        grade = "B";
        else if (score <90 && score >= 87)
        grade = "B+";

        else if (score <93 && score >= 90)
        grade = "A-";

        else
          grade = "A";



        System.out.printf("\nScore entered: %f%n", score);
        System.out.printf("Final grade: %s%n", grade);


      }
    }
}
