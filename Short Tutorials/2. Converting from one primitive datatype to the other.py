#!/usr/bin/Python

#THIS HELPS YOU UNDERSTAND SOME PRIMITIVE DATATYPES IN PYTHON

"""
NOTES
Previously we learnt about primitive datatypes
Now we are going to convert one datatype to another, Example str to int, int to float, float to int,etc.

REASONS TO CONVERT ONE PRIMITIVE DATATYPE TO ANOTHER
    There are many reasons we will want to convert one datatype to another in our programs.
    You can skip this sectionand go to how we convert datatypes
    **Some Reasons**
    1. Performing calculations with input data. The input() returns a string by default.
        Example: run this command type(input()) and enter any datatype value, it is going to output str
        There is the need to convert the str to int or float before you can make calculations with it
    2. Performing functions with data. Str datatype has many methods that are not available to int and float types
        E.g you can count number of characters, get a range of characters, get the first or last character,
         etc with strings. You can't do these with int and float values. There is the need to convert
         your float or int datatype to string if you want to perform those operations.
    3. etc.

HOW WE CONVERT DATATYPE
"""
#Converting to INT
data1 = "hey" # A str :NB- Trying to convert data1 to int will result in an error because alphabets can't convert to numbers
data2 =  "6532" # A str value because it is in quotes too
data3 = 78.64 #This is a float value, because it has a decimal part
data4 = True #This is a boolean value
data5 = 38 #int value

#result1 = int(data1) -> I am commenting it because it will result in an error, read the comment on data1 above
result2 = int(data2) #result now holds the int instance of data2
print("result 2 is of ",type(result2),"with value",result2) #The type is now int and the value is 6532

result3 = int(data3) #result now holds the int instance of data3, beware that the decimal part will be stripped off
print("result 3 is of ",type(result3),"with value",result3)

result4 = int(data4) #result now holds the int instance of data4 : True is converted to 1, and false to 0
print("result 4 is of ",type(result4),"with value",result4)

print("'2'+'3' = ",("2"+"3")) # "2"+"3" returns 23, string values are concatenated(combined)
print("2 + 3 = ",(2+3)) #This prints 5, because integer values are added


#Converting to Str
result1 = str(data3) #This converts the float value to string value
result2 = str(data4) #This converts the bool value to string by adding quotes
result3 = str(data5) #This converts the int value in data5 to string

#Converting to Float -> You can print out the values as I have done in the first part
#data1 cannot be converted to float
result2 = float(data2) #data2 is a string value. It is converted to float by removing the quotes and adding a decimal part
result3 = float(data3) #data3 is already a float value, no changes will be made
result4 = float(data4) # The boolean value is converted to a float value, output will be 1.0
result5 = float(data5) #data5 is an int value, it is converted to float, by adding decimal part to the number

#You can convert a value to boolean by using bool(value)
#You can also convert a value to complex number by using complex(value)
