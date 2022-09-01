#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

print("Python Looping Structures");

print("\nProgram Requirements\n"+
"Print while loop\n"+
"Print for loops using range() function, and implicit and explicit lists\n"+
"Use break and continue statements\n"+
"Replicate Display Below\n");

print("1. While Loop:");
counter = 1
while counter < 4:
    print(counter)
    counter += 1
print()

print("2. For Loop: using range() function with one arg:");
for i in range(4):
    print(i)
print()

print("3. For Loop: using range() function with two args:")
for i in range(1,4):
    print(i)
print()

print("4. For Loop: using range() function with three args (interval 2):")
for i in range(1,4,2):
    print(i)
print()

print("5. For Loop: using range() function with three args (negative interval 2):")
for i in range(3,0,-2):
    print(i)
print()

print("6. For loop: using implicit list (list not assigned to a variable):")
for i in [1,2,3]:
    print(i)
print()

print("7. For loop: using explicit list of strings:")
states = ["Michigan","Alabama","Florida"]
for state in states:
    print(state)
print()

print("8. For loop: using break statement (stops loop):")
for state in states:
    if state == "Alabama":
        break
    print(state)
print()

print("9. For loop: using continue statement (stops and continues with next):")
for state in states:
    if state == "Alabama":
        continue
    print(state)
print()

print("10. Print list length:")
print(len(states))
print()