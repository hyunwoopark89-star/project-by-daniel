#functions and modules
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


#function call and storing the result in a variable
def add(a,b):
    return a + b

result=add(5,9)
print(result)
print(f"result of add(5, 9) is {result}.")


#default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Bob")

#built in math module
import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(25))

