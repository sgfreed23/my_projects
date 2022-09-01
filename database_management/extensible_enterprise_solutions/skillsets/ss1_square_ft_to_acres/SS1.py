#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Square Feet to Acres")
print("\nProgram Requirements\n"+
"Research: number of square feet to acres\n"+
"Must use float data type for user input and calculaton\n"+
"Format and round conversion to two decimal places\n")
ft = float(input("Enter square feet: "));
acre = ft/43560;

print("\nOutput:");
print(f'{ft:,.2f} square feet = {acre:.2f} acres');
