#Understanding Rounding the numbers to nearest integer and understanding floating point values

#taking input from user in float format using the built in fn "float()"

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# The round() function rounds a number to the nearest integer. In Python, it uses Banker's Rounding: numbers with a fractional part of exactly .5 are rounded to the nearest even integer. Numbers below or above .5 are rounded down or up to nearest integer normally.

z = round(x + y)

print (fr"Result = {z}" )


