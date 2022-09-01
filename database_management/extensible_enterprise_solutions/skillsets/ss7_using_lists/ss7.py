#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021
print("Python Lists");
print("\nProgram Requirements\n"+
"1.List (Python data structures): mutable, ordered sequence of elements\n"+
"2.Lists are mutable/changeable--that is, can insert, update, delete\n"+
"3.Create list - using square brackets [list]: my_list = ['cherries', 'apples', 'bananas', 'oranges']\n"+
"4.Create a program that mirrors the following IPO (inout/process/output) format\n");
print("\nUser Input:")
numElements = int(input("Enter number of list elements: "))

elements = []

for i in range(numElements):
    elements.append(input("Enter list element " + str(i+1) + ": "))

print("\nOutput:")
print("Print the list:")
print(elements)

newElement = input("\nEnter a new element to insert: ")
newElementPos = int(input("Enter index position of new element: "))

elements.insert(newElementPos,newElement)
print("\nNew Element inserted into the list:")
print(elements)

print("\nNumber of elements in the list:")
print(len(elements))

print("\nSort elements in list alphabetically:")
elements.sort()
print(elements)

print("\nReverse List:")
elements.reverse()
print(elements)


print("\nRemove last list element:")
elements.pop()
print(elements)

print("\nDelete second element from list by *index*:")
elements.pop(1)
print(elements)

delElement = input("\nEnter an element to delete: ")
print("\nDelete element from list by *value* (" + delElement + "):")
elements.remove(delElement)
print(elements)

print("\nDelete all elements from list:")
elements = []
print(elements)