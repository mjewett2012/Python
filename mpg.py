# Michael Jewett
# 08/24/2023
# Exercise 2-1

#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of fuel used:\t"))
fuel_cost = float(input("Enter fuel price per gallon:\t"))
# calculate miles per gallon
#mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 1)
tfc = round(gallons_used * fuel_cost, 1)    
cpm = round( fuel_cost / mpg, 1)        
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Fuel cost:\t\t{tfc}")
print(f"Cost Per Mile:\t\t{cpm}")
print()
print("Bye!")


