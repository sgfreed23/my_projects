import java.util.*;
import java.io.*;

public class ss4_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program lists files and subdirectories of user-specified directory.");
        System.out.println();
    }

    public static void directoryInfo() {
       Scanner sc = new Scanner(System.in);
       String myDir = "";
       System.out.print("Please enter directory path: ");
       myDir = sc.nextLine();
       File directoryPath = new File(myDir);
       File filesList[] = directoryPath.listFiles();

       System.out.println("List files and directories in specified directory: ");

       for (File file : filesList) {
         System.out.println("Name: " + file.getName());
         System.out.println("Path: " + file.getPath());
         System.out.println("Size(Bytes): " + file.length());
         System.out.println("Size (KB): " + file.length() / (1024));
         System.out.println("Size (MB): " + file.length() / (1024 * 1024));
         System.out.println();
       }

       System.out.println("-----------------------------------");

     }
}
