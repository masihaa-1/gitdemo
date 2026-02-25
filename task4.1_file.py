# Module: Files and Exception Handling
# Task 1: Read a File and Handle Errors
import os
print("Current Working Directory:",os.getcwd())
try:
    # Attempting to open the file in read mode
    file = open("sample.txt.txt", "r")

    print("Reading file content:")

    # Reading the file line by line
    line_number = 1
    for line in file:
        # Printing each line with line number
        print("Line", line_number, ":", line.strip())
        line_number += 1

    # Closing the file after reading
    file.close()

# Handling the error if file does not exist
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")