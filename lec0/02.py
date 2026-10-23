#Exploring parameters (parameters is just a variable defined in a function to receive a value while the argument is the actual value a parameter receives)

print("what's your name??", end = " ")
name = input()
print("Hii", name)

# Here the end = " " is a keyword or named parameter which we used to put a space just after what's your name?? gets printed
# end is a prameter passed to print function while " " this space inside double quotation is argument passed to the parameter
# By default when we use the print function the value of end is set to end = "\n", which means as soon as print is executed the cursor moves to new line 
# Tutor also taught parameter "sep" whose role is to add a space between two objects inside the print Function, the code below demonstrates that 

age = input("what's your age?? ")
height = input("what's your height?? ")
print("your age is: ", age, "your height is:", height, sep ="???")

"""
We pass 4 objects to print(): "your age is:", age, "your height is:", height.
By default, sep=" " separates them with spaces, but sep="???" separates them with ???.
Since there are 4 objects, ??? appears 3 times in the output.

"""

# sep is a keyword parameter, and "???" is its argument in the above code. 
