#!/usr/bin/python
#This program generates random numbers within the given range
import random
strt,end = 1,0
print("Generates a random number within a range. Example: 1-50")
while strt >= end:
    strt = int(input("Enter starting value: "))
    end = int(input("Enter ending value: "))
    if strt>end:
        print("Start value cannot be greater than end\n\n")

total = int(input("How many numbers do you want to generate: "))
print("Generating",total,"random digits")
for i in range(total):
    print(random.randint(strt,end))


#Check in the intermediate section for improved version of this program
