#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Python Selection Structures");

print("\nProgram Requirements\n"+
"Use Python selection structure\n"+
"Prompt user for two numbers, and a suitable operator\n"+
"Test for correct numeric operator\n"+
"Replicate Display Below\n");

print("\nPython Calculator");

num1 = float(input("Enter num1: "));
num2 = float(input("Enter num2: "));

print("\nSuitable Operators: +,-,*,/,// (integer division), %(modulo operator),**(power)");
operator = str(input("Enter Operator:"));

result = 0;
if operator == "+":
    result = num1 + num2;
    print(result);

if operator == "-":
    result = num1 - num2;
    print(result);

if operator == "*":
    result = num1 * num2;
    print(result);

if operator == "/":
    result = num1 / num2;
    print(result);

if operator == "//":
    result = num1 // num2;
    print(result);

if operator == "%":
    result = num1 % num2;
    print(result);

if operator == "**":
    result = num1 ** num2;
    print(result);

if operator != "+" and operator != "-" and operator != "*" and operator != "/" and operator != "//" and operator != "%" and operator != "**":
    print("Incorrect operator!")
    exit;

