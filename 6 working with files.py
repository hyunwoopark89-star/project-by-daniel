with open("example.txt", "w") as file:
    file.write("Hello, this is a test file!\n")
    file.write("Python makes file handling easy.")
# As soon as the indentation ends here, 
# Python automatically "closes" the file for you.
# It is now safe.

# Reads the entire file into one big string
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reads every line into a list of strings
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines[0]) # Prints just the first line

with open("example.txt", "a") as file:
    file.write("\nAppending a new line!")

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
# strip() removes the newline character (\n) at the end of each line

import os
if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        print(file.read())
else:
    print("File not found.")

#This is a more specific exception handling for file not found errors.
try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")