#!/usr/bin/Python

#THIS HELPS YOU UNDERSTAND SOME PRIMITIVE DATATYPES IN PYTHON

"""
NOTES
Primitive datatypes are datatypes that holds a single value
Here are 5 primitive datatypes INT, STR, FLOAT, COMPLEX, BOOL
**INT**
INT -> or Integers are whole number values, which is either positive, negative or zero
STR -> or Strings is any value which is not a number. It can be any character, or combination of characters.
        It is always enclosed in a string. Note that- str is a composite datatype in some programming languages
        But in python, it behaves as both composite and primitive datatypes
FLOAT -> Float numbers are numbers that have decimal parts, it can also be positive or negative.
        E.g include irrational numbers
COMPLEX -> Complex numbers are numbers that have a real number and an imaginary number
BOOL -> Its just a statement that evaluates to true or false, 0 or 1
BELOW ARE DEMONSTRATIONS OF PRIMITIVE DATATYPES IN PYTHON
RUN THIS CODE AND COMPARE THE CODE TO THE OUTPUT TO UNDERSTAND PRIMITIVE DATATYPES BETTER
"""

#INT
positive_int = 5
negative_int = 3
zero_int = 0
int1 = 5 // 2
int2 = 5 * 3
print(positive_int,"belongs to",type(positive_int))
print(negative_int,"belongs to",type(negative_int))
print(zero_int,"belongs to",type(zero_int))
print(int1,"belongs to",type(int1))
print(int2,"belongs to",type(int2))
print() #This prints a new line

#STR
str1 = "5" #This is a string because it is enclosed in quoatations. You can't perform calculations with it
str2 = "Hello"
str3 = "Q33N" #Search Q33N in google and I promise you will love what you will find
print(str1,"belongs to",type(str1))
print(str2,"belongs to",type(str2))
print(str3,"belongs to",type(str3))
print() #This prints a new line

#FLOAT
positive_float = 5.38
negative_float = -3.8
float1 = 5.0
float2 = 5 / 2 #The results of this expression is a float
float3 = 5 * 3.0 #if any of the value is a float, the result is a float
print(positive_float,"belongs to",type(positive_float))
print(negative_float,"belongs to",type(negative_float))
print(float1,"belongs to",type(float1))
print(float2,"belongs to",type(float2))
print(float3,"belongs to",type(float3))
print()

#COMPLEX - j is added to the imaginary part of the number
complex1 = 3j
complex2 = 2+3j
complex3 = 6-0j
print(complex1,"belongs to",type(complex1))
print(complex2,"belongs to",type(complex2))
print(complex3,"belongs to",type(complex3))
print()
#BOOL
bool1 = 2 > 5 #This evaluates to false
bool2 = (5-2)==3 #This evaluates to true
bool3 = True #True evaluates to true
bool4 = False #False evaluates to false
bool5 = "33".isalpha() #This evaluates to false because 33 is a number not alphabet
bool6 = "k" in "Kamaldeen" #This evaluates to False, because k is not found, check the case
bool7 = "K" in "Kamaldeen" #This evaluates to True, because K is found
print("2 > 5 evaluates to",bool1)
print("(5-2)==3 evaluates to",bool2)
print("True evaluates to",bool3)
print("False evaluates to",bool4)
print("\"33\".isalpha() evaluates to",bool5)
print("\"k\" in \"Kamaldeen\" evaluates to",bool6)
print("\"K\" in \"Kamaldeen\" evaluates to",bool7)

#NEXT IS COMPOSITE DATATYPES
