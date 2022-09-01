import java.util.*;

public class vehicledemo
{
 public static void main(String[] args)
 {
  String mk = "";
  String md = "";
  int yr = 0;
  float sp = 0.0f;
  Scanner sc = new Scanner(System.in);

  System.out.print("\n/////Below are base class default constructor values://///");
  vehicle v1 = new vehicle();
  System.out.println("\nMake = " + v1.getMake());
  System.out.println("Model = " + v1.getModel());
  System.out.println("Year = " + v1.getYear());

  System.out.println("\n/////Below are base class user-entered values://///");

  System.out.print("\nMake: ");
  mk = sc.nextLine();

  System.out.print("Model: ");
  md = sc.nextLine();

  System.out.print("Year: ");
  yr = sc.nextInt();

  vehicle v2 = new vehicle(mk, md, yr);
  System.out.println("\nMake = " + v2.getMake());
  System.out.println("Model = " + v2.getModel());
  System.out.println("Year = " + v2.getYear());

  System.out.println("\n/////Below usinf setter methods to pass literal values, then print() method to display values://///");
  v2.setMake("Chevrolet");
  v2.setModel("Corvette Z06");
  v2.setYear(2023);
  v2.print();
  System.out.println();
 }
}