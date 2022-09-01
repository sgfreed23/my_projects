#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Python Sets");
print("\nProgram Requirements\n"+
"1. Sets (Python data structures): mutable, heterogeneous, unordered sequence of elements, *but* cannot hold duplicate values\n"+
"2. Sets are mutable/changeable--that is, can insert, update, delete\n"+
"3. While sets are mutable/changeable, they *cannot* contain other mutable items like list, set or dictionary that is, elements contained in set must be immutable\n"+
"4. Also, since sets are unordered, cannot use indexing(or, slicing) to access, update, or delete elements\n"+
"5. Two methods to create sets:\n"+
"   a. Create set using curly brackets: {set}: my_set = {1,3.14,2.0,'four','five}\n"+
"   b. Create set using set() function: my_set = set(<iterable>)\n"+
"6. Create a program that mirrors the following IPO (inout/process/output) format\n");

print("\nUser Input: Hard coded--no user input.")

my_set = {1, 3.14, 2.0, 'four', 'Five'}
print("\nPrint my_set created using curly brackets:")
print(my_set)

print("\nPrint type of my_set:")
print(type(my_set))

my_set1 = set([1, 3.14, 2.0, 'four', 'Five'])
print("\nPrint my_set1 created using set() method with list:")
print(my_set1)

print("\nPrint type of my_set1:")
print(type(my_set1))

my_set2 = set((1, 3.14, 2.0, 'four', 'Five'))
print("\nPrint my_set2 created using set() method with tuple:")
print(my_set2)

print("\nPrint type of my_set2:")
print(type(my_set2))

print("\nLength of my_set:")
print(len(my_set))

print("\nDiscard 'four' from my_set:")
my_set.discard('four')
print(my_set)

print("\nRemove 'Five' from my_set:")
my_set.remove('Five')
print(my_set)

print("\nLength of my_set:")
print(len(my_set))

print("\nAdd element to my_set (4) using add() method:")
my_set.add(4)
print(my_set)

print("\nLength of my_set:")
print(len(my_set))

print("\nMinimum number in my_set:")
print(min(my_set))

print("\nMaximum number in my_set:")
print(max(my_set))

print("\nSum of numbers in my_set:")
print(sum(my_set))

print("\nDelete all set elements in my_set:")
my_set.clear()
print(my_set)

print("\nLength of my_set:")
print(len(my_set))