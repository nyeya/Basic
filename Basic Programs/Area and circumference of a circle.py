#!usr/bin/python

#Finding Area and circumference of a circle
import math

radius = float(input("Enter Radius: ")) #Take radius as input from user
area = math.pi * radius**2   #Calculates the area and stores it
circumference = 2 * math.pi * radius #Calculates the circumference and stores it

print('The area of the circle is', area) #Prints the area of the circle
print('The circumference of the circle is',circumference)  #Prints the circumference of the circle
