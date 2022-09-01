#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

def program_requirements():
    print("Temperature Conversion Program");
    print("\nProgram Requirements\n"+
    "1. Program converts user-entered temperatures into Farenheit or Celsius scales\n"+
    "2. Program continues to prompt for user entry until no longer requested\n"+
    "3. Note: upper or lower case letteres permitted. though incorrect entries are not permitted\n"+
    "4. Note: Program does not validate numeric data (optional requirement)\n");


def convert_temperature():
    print("\nInput:")
    counter = str(input("Do you want to convert a temperature (y or n)? "))
    print("\nOutput: ")
    
    while True:
        while (counter == 'y' or counter == 'Y'):
            type = str(input("Fahrenheit to Celsius? Type 'f', or Celsius to Fahrenheit? Type 'c': "))
            if(type == 'F' or type == 'f'):
                ftemp = float(input("Enter temperature in Fahrenheit: "))
                ctemp = (ftemp - 32) / 1.8
                ltemp = str(ctemp)
                print("Temperature in Celsius = " + ltemp)
                print()
                counter = input("Do you want to convert another temperature (y or n)? ")

            elif(type == 'c' or type == 'C'):
                ctemp2 = float(input("Enter temperature in Celsius: "))
                ftemp2 = (ctemp2 * 1.8) + 32
                ltemp2 = str(ftemp2)
                print("Temperature in Fahrenheit: " + ltemp2)
                print()
                counter = input("Do you want to convert another temperature (y or n)? ")

            else:
                print("Incorrect entry. Please try again.\n")
                counter = input("Do you want to convert a temperature (y or n)? ")
                break
        else:
            print()
            print("Thank you for using our Temperature Conversion Program!\n")
            break