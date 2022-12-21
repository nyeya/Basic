#!/usr/bin/python

#Multiplication table generator

numb = int(input("Enter a number: ")) #Enter a number to draw the multiplication

#Use a for loop to make a multiplication table from 1 to 12 of the chosen number
for i in range(1, 13):
    print(numb, 'x', i, '=', numb*i)
