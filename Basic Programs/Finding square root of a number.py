#!/usr/bin/python

#Finding Square root of a whole number

number = int(input("Enter a number: ")) #Takes the number as input

#Method 1
print("Method 1")
print("Square root of",number,"is",number**0.5) #This method raises the number to the power half and prints the results

#Method 2
print("Method 2")
from math import sqrt       #Imports the sqrt function from math module
print("Square root of",number,"is",sqrt(number)) #Uses the sqrt function to print the square root of the number
