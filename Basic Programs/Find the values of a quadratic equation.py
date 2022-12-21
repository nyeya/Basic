#!/usr/bin/python

#Solve the quadratic equation of the form ax^2 + bx + c = 0 using the general formula
#General formular x1 = (-b + sqrt(discriminant)) / 2a

# import math module
from cmath import sqrt

a = int(input("Enter \'a\' value: "))
b = int(input("Enter \'b\' value: "))
c = int(input("Enter \'c\' value: "))

# calculate the discriminant Formular: b^2 - 4ac
discriminant = (b**2) - (4*a*c)
# find the x values
x1 = (-b-(sqrt(discriminant)))/(2*a)
x2 = (-b+sqrt(discriminant))/(2*a)

print("x1 = ",x1)
print("x2 = ",x2)
