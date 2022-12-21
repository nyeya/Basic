#!/usr/bin/python

#Checking for a prime number manually

#A function that returns true if the number passed is a prime else returns false
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: ")) #Allows a user to enter a number
print("Number is prime" if is_prime(number) else "Number not prime") #Prints a statement based on the return of the function
