import java.util.Scanner;

public class ss1_methods{
    public static void getRequirements(){
        
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program evaluates integers as even or Odd.");
        System.out.println("Note: Program does *not* check for non-numeric characters.");
        System.out.println();

    }

    public static void evaluateNumber(){

        //initialize variables, create Scanner object, capture user input
        int x = 0;
        System.out.print("Enter Integer: ");
        Scanner sc = new Scanner(System.in);
        x = sc.nextInt();

        if (x % 2 == 0){
            System.out.println(x + " is an even nmumber.");
        }else{
            System.out.println(x + " is an odd number.");
        }

    }


}
