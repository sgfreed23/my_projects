#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("IT/ICT Student Percentage");

print("\nProgram Requirements\n"+
"Find nmber of IT/ICT students in class\n"+
"Cacuclate IT/ICT Student Percentage\n"+
"Must use float data type\n"+
"Format, right-align, and round conversion to two decimal places\n");

print("\nUser Input:");
it_stud = float(input("\nEnter number of IT students: "));
ict_stud = float(input("\nEnter number of ICT students: "));

total_stud = it_stud + ict_stud;
it_stud_percent = round(((it_stud/total_stud)*100),2);
ict_stud_percent = round(((ict_stud/total_stud)*100),2);

print("\nOutput:");
print("\nTotal Students: " + str(total_stud).rjust(18));
print("IT student percentage: " + str(it_stud_percent).rjust(10) + "%");
print("ICT student percentage: " + str(ict_stud_percent).rjust(9) + "%");


