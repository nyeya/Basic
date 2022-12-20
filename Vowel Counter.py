#!/usr/bin/python

#Count vowels in a word

word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0

for char in word:
    if char in vowels:
        count += 1

print('Number of vowels:', count)
