#!/usr/bin/python
#Swapping variables in python

#Method 1:
print("Method 1")
#Swap x and y values using a temporal variable

x = 5 #You can change the value of x
y = 8 #You can change the value of y
print("The values of x and y before swapping:")
print("x =",x,"y =",y)
temp = x
x = y
y = temp
print("The values of x and y after swapping:")
print("x =",x,"y =",y) # Same print statement as the first one but now the values of x and y have changed

#Method 2
print("\nMethod 2")
#Swapping without using temporal variable
a = 5
b = 8
print("The values of a and b before swapping:")
print("a =",a,"b =",b)
a,b = b,a #This does the magic of swapping the variable, not a magic though
print("The values of a and b after swapping:")
print("a =",a,"b =",b) #The same print statement as the first but the values of a and b swapped
