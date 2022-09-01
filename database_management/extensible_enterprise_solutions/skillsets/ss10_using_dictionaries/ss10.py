#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Python Dictionaries");
print("\nProgram Requirements\n"+
"1. Dictionaries (Python data structures): unordered key:value pairs\n"+
"2. Dictionary: an associative array (also known as hashes)\n"+
"3. Any key in a dictionary is associated (or mapped) to a value (i.e., any python data type)\n"+
"4. Keys: must be of immutable type (string, number or tuple with immutable elements) and must be unique\n"+
"5. Values: can be any data type and can repeat\n"+
"6. Create a program that mirrors the following IPO (inout/process/output) format\n"+
"   a. Create empty dictionary, using  curly braces: {}: my_dictionary = {}\n"+
"   b. Use the following keys:fname, lname, degree, major, gpa\n");

my_dictionary = {}
    
print("\nInput:")

my_dictionary['fname'] = str(input("First Name: "))
my_dictionary['lname'] = str(input("Last Name: "))
my_dictionary['degree'] = str(input("Degree: "))
my_dictionary['major'] = str(input("Major: "))
my_dictionary['gpa'] = float(input("GPA: "))

print("\nOutput:")

print("Print my_dictionary:")
print(my_dictionary)

print("\nReturn view of dictionary's key:value pair (built-in function):")
print(my_dictionary.items())

print("\nReturn view object of all keys (built-in function):")
print(my_dictionary.keys())

print("\nReturn view object of all values (built-in function):")
print(my_dictionary.values())

print("\nPrint only first and last names, using keys:")
print(my_dictionary['fname'] + " " + my_dictionary['lname'])

print("\nPrint only first and last names, using get() function:")
print(my_dictionary.get('fname') + " " + my_dictionary.get('lname'))

print("\nCount number of items (key:value pairs):")
print(len(my_dictionary))

print("\nRemove last dictionary item:")
my_dictionary.popitem()
print(my_dictionary)

print("\nDelete major from dictionary (using key):")
my_dictionary.pop('major')
print(my_dictionary)

print("\nReturn object type:")
print(type(my_dictionary))

print("\nDelete all items from dictionary:")
my_dictionary.clear()
print(my_dictionary)