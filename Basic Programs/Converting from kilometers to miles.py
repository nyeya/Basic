#!/usr/bin/python
#Converting Kilometers to Miles

kilometers = float(input("Enter kilometer distance: ")) # Taking kilometer value from the user

conversion_fact = 0.621371 # conversion factor

# calculate the distance in miles
miles = kilometers * conversion_fact
print("{:.2f} kilometers is equal to {:.2f} miles".format(kilometers,miles))
