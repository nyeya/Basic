#!/usr/bin/python

#Finding largest number in a list using a for loop

numbers = [3, 7, 2, 9, 12, 4] #Create a list of numbers, you can change the list here

#Method 1
print("Method 1")
max_num = numbers[0] # We take the first number as our largest number
#Loop through each number using a for loop
for num in numbers:
    #Compares each number to the stored number
    if num > max_num:
        #Re define max_num if a number is greater than the current max_num
        max_num = num
print('Largest number:', max_num) #Prints the largest number

#You can also use this one line of code in place of the for loop
print("\nMethod 2")
print("Largest number :",max(numbers))
