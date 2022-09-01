public class ss2_methods {
    public static void getRequirements(){
        
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program loops through array of floats.");
        System.out.println("Use following values: 2.0, 2.1, 3.2, 4.3, 5.4");
        System.out.println("Use following loop structures: for, enhanced for, while, do...while.");
        System.out.println("Note: Pretest loops: for, enhanced for, while. Posttest loop: do...while.");
        System.out.println();

    }

    public static void loopStructures(){
        Float[] floats = { 1.0f, 2.1f, 3.2f, 4.3f, 5.4f};

        System.out.println("for loop:");
        for (int i = 0; i < floats.length; i++) {
            System.out.println(floats[i]);
        }
        System.out.println();

        System.out.println("Enhanced for loop:");
        for (Float i : floats){
            System.out.println(i);
        }
        System.out.println();

        System.out.println("while loop:");
        int i = 0;
        while (i<5){
            System.out.println(floats[i]);
            i++;
        }
        System.out.println();

        System.out.println("do ... while loop:");
        int d = 0;
        do {
            System.out.println(floats[d]);
            d++;
        }
        while(d<5);
    } 
}
