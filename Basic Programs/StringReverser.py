#!/usr/bin/python

#Reverse a string, sentence or a number

word = input("Enter a word: ") #Take a string to reverse, you can also enter a number
reversed_word = word[::-1] #This tricks uses slice method to reverse the word

print("The reverse of",word," - ",reversed_word) #Print out the reversed word
