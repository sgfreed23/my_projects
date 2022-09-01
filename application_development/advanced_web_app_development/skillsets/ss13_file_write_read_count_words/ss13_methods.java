import java.util.*;
import java.io.*;

public class ss13_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Brennan O'Hara\n");
        System.out.println("Program Requirements:");
        System.out.println("Program captures user input, writes to and reads from same file, and counts number of words in file.");
        System.out.println("Hint: use hasNext() method to read number of words (tokens).");
        System.out.println();
    }


    public static void readFile()
    {
       String myFile = "filecountwords.txt";

       try {
	           File file = new File(myFile);
             PrintWriter writer = new PrintWriter(file);
	           Scanner scnr = new Scanner(System.in);
	           String test = "";
	           System.out.print("Please enter line of text: ");
	           test = scnr.nextLine();
	           writer.write(test);
	           System.out.println("Saved to file \"" + myFile + "\"");
	           writer.close();
	           Scanner read = new Scanner(new FileInputStream(file));
	           int count = 0;
	               while (read.hasNext())
	                 {
		                   read.next();
		                   count++;
	                 }
	            System.out.println("Number of words: " + count);

            }

      catch(IOException ex) {
	    System.out.println("Error writing to file " + myFile + "");

    }

	}
}
