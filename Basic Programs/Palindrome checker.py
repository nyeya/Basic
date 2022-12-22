#!/usr/bin/python
"""
Palindrome Checker
Palindrome is a words that is the same when read both forward and backwards
Examples of Palindrome: level, mom, noon, refer, madam, aibohphobia (means fear of palindromes), etc
"""
#Palindrome Checker
word = input("Enter a word: ").lower() #Change the entered word to lowercase before storing for caseless comparism


#Method 1
print("Method 1")
#reverse the word and store it in a new variable
rev_word = reversed(word)
# check if the string is equal to its reverse
if list(word) == list(rev_word):
    print(word,"is a palindrome.")
else:
    print(word,"is not a palindrome.")


#Method 2
print("\nMethod 2")
#use slice method
if(word==word[::-1]):
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")
