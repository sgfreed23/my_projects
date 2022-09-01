public class ss3_methods {
    public static void getRequirements(){
        
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program loops through array of strings.");
        System.out.println("Use following values: dog, cat, bird, fish, insect.");
        System.out.println("Use following loop structures: for, enhanced for, while, do...while.");
        System.out.println("Note: Pretest loops: for, enhanced for, while. Posttest loop: do...while.");
        System.out.println();

    }

    public static void loopStructures(){
        String[] animals = {"dog", "cat", "bird", "fish", "insect"};

        System.out.println("for loop:");
        for (int i = 0; i < animals.length; i++) {
            System.out.println(animals[i]);
        }
        System.out.println();

        System.out.println("Enhanced for loop:");
        for (String i : animals){
            System.out.println(i);
        }
        System.out.println();

        System.out.println("while loop:");
        int i = 0;
        while (i<5){
            System.out.println(animals[i]);
            i++;
        }
        System.out.println();

        System.out.println("do ... while loop:");
        int d = 0;
        do {
            System.out.println(animals[d]);
            d++;
        }
        while(d<5);
    }    
}
