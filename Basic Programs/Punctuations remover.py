#!/usr/bin/python

#punctuations remover
punctuations = "!()-[]{};:'\"\\,<>./?@#$%^&*_~" #You can add your own characters as well

word = input("Enter your word or statement: ")

# Remove punctuation from the string
updated_word = "" #This holds our new string without punctuations
for char in word:
    if char not in punctuations:
        updated_word += char

print("\nResults:")
print(updated_word) # Display our unpunctuated string
