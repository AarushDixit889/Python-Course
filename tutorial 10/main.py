# Project 1 - Calculator
from math import *
print("Welcome to the calculator")
while True:
    expression=input("Enter the expression:\t")
    print(eval(expression))
    if expression=="quit":
        quit()