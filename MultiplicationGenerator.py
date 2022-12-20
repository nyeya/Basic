#!/usr/bin/python

#Multiplication table generator

numb = int(input("Enter a number: "))

for i in range(1, 13):
    print(numb, 'x', i, '=', numb*i)
