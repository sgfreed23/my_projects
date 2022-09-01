public class ss1_methods {
    public static void getRequirements()
    {
        System.out.println("Developer: Samuel Freed");
        System.out.println("Program lists system properties.\n");
    }

    public static void showProps()
    {
        System.out.println("System File Path Seperator: " + System.getProperty("file.separator"));
        System.out.println("Java Class Path: " + System.getProperty("java.class.path"));
        System.out.println("Java Installation Directory: " + System.getProperty("java.home"));
        System.out.println("Java Vendor Name: " + System.getProperty("java.vendor"));
        System.out.println("Java Vendor URL: " + System.getProperty("java.vendor.url"));
        System.out.println("Java Version Number: " + System.getProperty("java.version"));
        System.out.println("JRE Version: " + System.getProperty("java.runtime.version"));
        System.out.println("OS architecture: " + System.getProperty("os.arch"));
        System.out.println("OS Name: " + System.getProperty("os.name"));
        System.out.println("OS Version: " + System.getProperty("os.version"));
        System.out.println("Path Seperator used in java.class.path: " + System.getProperty("path.separator"));
        System.out.println("User Working Directory: " + System.getProperty("user.dir"));
        System.out.println("User home directory: " + System.getProperty("user.home"));
        System.out.println("User account name: " + System.getProperty("user.name"));
    }
}
