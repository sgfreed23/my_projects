import java.util.Scanner;

public class ss4_methods {
    public static void getRequirements(){
        
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program evaluates user-centered characters.");
        System.out.println("Use following characters: W or w, C or c, H or h, N or n.");
        System.out.println("Use following decision structures: if...else, and switch");
        System.out.println();

    }

    public static void decisionStructures(){
        System.out.println("Phone types: W or w (work), C or c (cell), H or h (home), N or n (none)");
        System.out.print("Enter phone type: ");
        Scanner src = new Scanner(System.in);
        char myPhone = src.next().charAt(0);
        
        System.out.println("\nif...else: ");
        if (myPhone == 'W' || myPhone == 'w'){
            System.out.println("Phone type: Work");
        } else if(myPhone == 'C' || myPhone =='c'){
            System.out.println("Phone type: Cell");
        } else if(myPhone == 'H' || myPhone == 'h'){
            System.out.println("Phone type: Home");
        } else if(myPhone == 'N' || myPhone == 'n'){
            System.out.println("Phone type: None");
        } else {
            System.out.println("Incorrect character entry");
        }

        System.out.println("\nswitch: ");

        switch (myPhone) {
            case 'W':
            case 'w': 
                System.out.println("Phone type: work");  
                break;
            case 'C':
            case 'c':
                System.out.println("Phone type: cell");
                break;
            case 'H':
            case 'h':
                System.out.println("Phone type: home");
                break;
            case 'N':
            case 'n':
                System.out.println("Phone type: none");
                break;
            default:
                System.out.println("Incorrect character entry.");
                break;
            }
    }
}
