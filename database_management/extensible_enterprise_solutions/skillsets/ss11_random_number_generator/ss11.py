#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

import random

print("Puesdo-Random Number Generator");
print("\nProgram Requirements\n"+
"1. Get user beginning and ending integer values, and store in two variables\n"+
"2. Display 10 psuedo-random numbers between, and including, above values\n"+
"3. Must use ineger data types\n"+
"4. Example 1: Using range() and randint() functions\n"+
"5. Example 2: Using a list with range() and shuffle() functions\n");

start = 0
end = 0

print("\nInput: ")
start = int(input("Enter beginning value: "))
end = int(input("Enter ending value: "))

print("\nOutput:")
print("Example 1: Using range() and randint() functions:")
for item in range(10):
    print(random.randint(start,end), sep=",", end=" ")
print()

print("\nExample 2: Using a list, with range() and shuffle() functions:")
my_list = list(range(start, end + 1))
random.shuffle(my_list)
for item in my_list:
    print(item, sep=",", end=" ")
print()