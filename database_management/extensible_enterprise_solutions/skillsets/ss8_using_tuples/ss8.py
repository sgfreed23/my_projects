#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Python Tuples");

print("\nProgram Requirements\n"+
"1. Tuple (Python data structures): *immutable*(cannot be changed), ordered sequence of elements\n"+
"2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete\n"+
"3. Create tuple using parentheses (tuple): my_tuple1 = ('cherries', 'apples', 'bananas', 'oranges')\n"+
"4. Create tuple (packing), that is, *wihtout* using parentheses (aka tuple 'packing'): my_tuple2 = 1,2'three','four'\n"+
"5. Create tuple (unpacking), that is, assign values from tuple to sequence of variables: fruit1,fruit2,fruit3,fruit4 = my_tuple1\n"+
"6. Create a program that mirrors the following IPO (inout/process/output) format\n");
print("\nInput: Hard coded--no user input.")

my_tuple1 = ('cherries', 'apples', 'bananas', 'oranges')

my_tuple2 = 1, 2, "three", "four"

print("\nOutput:")

print("\nPrint my_tuple1:")
print(my_tuple1)

print("\nPrint my_tuple2:")
print(my_tuple2)

fruit1, fruit2, fruit3, fruit4 = my_tuple1
print("\nPrint my_tuple1 unpacking:")
print(fruit1, fruit2, fruit3, fruit4)

print("\nPrint third element in my_tuple2:")
print(my_tuple2[2])

print("\nPrint \"slice\" of my_tuple2 (second and third elements):")
print(my_tuple2[1:3])

print("\nReassign my_tuple2 using \"packing\" method.")
my_tuple2 = 5, 6, 7, 8

print("Print my_tuple2:")
print(my_tuple2)

print("\nPrint number of elements in my_tuple1: " + str(len(my_tuple1)))

print("\nPrint type of my_tuple1: " + str(type(my_tuple1)))

print("\nDelete my_tuple1: ")
del my_tuple1

print()