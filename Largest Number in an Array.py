#!/usr/bin/python

#Finding largest number in a list using a for loop

numbers = [3, 7, 2, 9, 12, 4]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print('Largest number:', max_num)

#You can also use this one line of code 
print("Largest is :",max(numbers))
