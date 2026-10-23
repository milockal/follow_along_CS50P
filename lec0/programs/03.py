#understanding the f-strings, r-strings, fr-strings .

# An f-string lets us insert variables or expressions directly into a string

name = input("what's your name?? ")
print(f"Hii, {name}!!")

# The output that we get from code in line 5,6 is "Hii, alex!!" and that's coz we put a "f" before opening quotation mark of print fn.
# Without "f" at beginning the output would have been "Hii, {name}!!",the "f" made program smarter by making sure {name} fetches value from name variable instead of printing the word "{name}" as it is.



#A raw string or r- string treats backslashes literally as \ instead of interpreting as escape sequences.

print(r"hello\nWorld")

# The output that we get from code in line 15 is "hello\nWorld" and that's coz we put a "r" before opening quotation mark of print fn which literally treated \n as word "\n " instead of interpreting it as new line.



# fr-string combines the power of f and r string together

name = input("what's your name?? ")
print(fr"Hii, {name}, //n")


# The output that we get from code in line 23, 24 is "Hii, alex, //n" and that's coz we put a "fr" before opening quotation mark of print fn which not only allowed us to use value from variable "name" variable instead of printing "{name}"" but also allowed us use literal "\n" instead of "\n" getting treated as escape chctr for new line.