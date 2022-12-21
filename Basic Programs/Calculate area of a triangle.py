#!/usr/bin/python
#Calculates the area of a triangle given three sides

# Three sides of the triangle is a, b and c:
x = float(input('Enter first side: '))
y = float(input('Enter second side: '))
z = float(input('Enter third side: '))

# calculate the semi-perimeter
semi = (x+ y + z) / 2

# Method 1:
print("Method 1")
# calculate the area
area = (semi*(semi-x)*(semi-y)*(semi-z)) **  0.5
print("The area of the triangle is {:.2f}".format(area)) #Prints the area to 2 decimal place

#Method 2
print("Method 2")
# calculate the area using the sqrt function
from cmath import sqrt
area=sqrt(semi*(semi-x)*(semi-y)*(semi-z))
print("Area of the triangle is: ",round(area,2)) # Rounds the area to 2 decimal place and print
