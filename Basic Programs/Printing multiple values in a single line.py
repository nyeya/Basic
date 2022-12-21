#!usr/bin/Python
# Demonstrating how to print multiple times on a single line using a for loop
#Printing on multiple lines, the default method
print("Printing on multiple lines")
for i in range(4):
    print(i)
print("Done now")
print("Thank you")
# Printing on a single line
print("\nPrinting on a single line")
for i in range(4):
    print(i,end=" ")
print("Done now",end=" ")
print("Thank you")
