#!/usr/bin/python

#Count vowels in a word

word = input("Enter a word: ").lower() #Make sure the input of the user is converted to lowercase
vowels = "aeiou" #Create a string of vowels
count = 0 #Initialise a counter
#A for loop to looop through each letter in the given word
for char in word:
    #If a letter is found in vowels
    if char in vowels:
        count += 1 #Increase the counter by 1

print('Number of vowels:', count) #Print out the number of counts
