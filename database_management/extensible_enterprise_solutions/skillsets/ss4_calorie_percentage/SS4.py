#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Calorie Percentage");

print("\nProgram Requirements\n"+
"Find calories per grams of fat, carbs, and protein\n"+
"Calculate percentages\n"+
"Must use float data types\n"+
"Format, right-align, and round conversion to two decimal places\n");
print("\nUser Input:")
fat = float(input("\nEnter total fat grams: "));
carb = float(input("\nEnter total carb grams: "));
protein = float(input("\nEnter total protein grams: "));

fat = round(((fat)* 9.0),2);
carb = round(((carb)* 4.0),2);
protein = round(((protein)* 4.0),2);

total = fat + carb + protein;

percentFat = round(((fat/total)*100),2);
percentCarb = round(((carb/total)*100),2);
percentProtein = round(((protein/total)*100),2);

print("\nOutput:");
print("\nType   " + "   Calorie   "+ "   Percentage");
print("Fat        " + str(fat).rjust(6)+ str(percentFat).rjust(15) + "%");
print("Carbs      " + str(carb).rjust(6)+ str(percentCarb).rjust(15) + "%");
print("Protein    " + str(protein).rjust(6)+ str(percentProtein).rjust(15) + "%");


