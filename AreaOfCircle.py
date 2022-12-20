#!user/bin/python

#Finding Area and circumference of a circle
import math

radius = float(input("Enter Radius: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius

print('The area of the circle is', area)
print('The circumference of the circle is',circumference)
