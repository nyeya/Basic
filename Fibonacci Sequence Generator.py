#!/usr/bin/python

#Generating a fibonacci sequence

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
        print(x,end=" ")

number = int(input("How many terms of Fibonacci should I generate: "))
fibonacci(number)
