#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Mielrs Per Gallon");

print("\nProgram Requirements\n"+
"Convert MPG\n"+
"Must use float data type for user input and calculation\n" +
"Format and round converstion to two decimal places\n");
print("\nUser Input:");
miles = float(input("Enter miles driven: "));

gallons = float(input("Enter gallons of fuel used: "));

mpg = (miles/gallons);

print("\noutput:");
print("\n" + str("{0:.2f}".format(miles))+" miles driven and " + str("{0:.2f}".format(gallons))
+ " gallons used = " + str("{0:.2f}".format(mpg)) + " mpg");