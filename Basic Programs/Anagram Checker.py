#!/usr/bin/python
"""
Anagram Checker
Words are said to be anagrams if we can rearrange the letters of one to form the other
Examples: "heart" & "earth", "care" & "race","binary" & "brainy","cat" & "act", "a gentleman" & "elegant man",etc
"""
# check if two strings are anagrams using sorted()
word1 = input("Enter the first word: ")
word1 = word1.lower() #Converts to lowercase to perform caseless comparism

word2 = input("Enter the second word: ")
word2 = word2.lower() #Converts to lowercase to perform caseless comparism

# check if length is same
#this method might not work with anagrams with different space characters
if(len(word1) == len(word2)):
    # sort the two words
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    if(word1_sorted == word2_sorted):
        print(word1,"and",word2,"are anagram of each other")
    else:
        print(word1,"and",word2,"are not anagram of each other")

else:
    print(word1,"and",word2,"are not anagram of each other")
