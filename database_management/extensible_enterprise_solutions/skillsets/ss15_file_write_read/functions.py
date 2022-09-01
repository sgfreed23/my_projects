#Developer: Samuel Freed
#Course: LIS4369
#Semester: Fall 2021

import os

def get_requirements():
    print("Write Read Program")
    print("Program Requirements:")
    print("1. Create write _read file subdirectory with two files: main.py and functions.py.")
    print("2. Use President Abraham Lincoln's Gettysburg Address: Full Text.")
    print("3. Write address to file.")
    print("4. Read address from same file.")
    print("5. Create Python Docstrings for functions in functions. py file.")
    print("6. Display Python Docstrings for each function in functions.py file.")
    print("7. Display full file path.")
    print("8. Replicate display below.")

    print("\nHelp on function write read file in module functions: ")
    print("Write_read file()")
    print("\tUsage: Calls two functions:")
    print("\t  1. file write() # writes to file")
    print("\t  2. file read() # reads from file")
    print("\tParameters: none")
    print("\tReturns: none")
    print("\nHelp on function file write in module functions:")
    print("file write()")
    print("\tUsage: creates file, and writes contents of global variable to file")
    print("\tParameters: none")
    print("\tReturns: none")
    print("\nHelp on function file_read in module functions:")
    print("file read()")
    print("\tUsage: reads contents of written file")
    print("\tParameters: none")
    print("\tReturns: none\n")


#def write_read_file():

#def file_write():

def file_read():
    with open('test.txt') as f:
        contents = f.read()
    print(contents)
    print("Full File Path: ")
    print(os.path.realpath(f.name))
