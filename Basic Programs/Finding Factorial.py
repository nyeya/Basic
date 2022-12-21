#!/usr/bin/python
#Finding factorial of a number using recursion

#A recursive function that takes a number as input and return its factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

number = int(input("Enter a number: ")) #Takes a number as input
print("The factorial of",number,"is",factorial(number)) #Calculates and prints the factorial of the input
