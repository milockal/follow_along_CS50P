#String Methods are built-in functions used to perform operations on strings, such as changing case, removing spaces, replacing characters, searching for text, and splitting a string.
#There are a lot of string methods and we will not discusss each one here.


print("What's your name", end = " ")
user = input()

#Remove whitespaces from str
user = user.strip()
# Note: The strip() method does not remove spaces between words in a string. It removes spaces from the beginning and the end of a string.

#Make startng character of each word to uppercase
user = user.title()


print ("Hii", user)

'''
We can use string methods individually by calling each method on a separate line, or we can combine multiple string methods in a single line.
For example, the code we wrote earlier can be shortened to:

print("What's your name", end=" ")
user = input()
user = user.strip().title()
print("Hii", user)

This code works in the same way as our previous code. The only difference is that we have combined the strip() and title() methods into a single line.
First, strip() removes the extra spaces from the beginning and end of the string. Then, `title()` capitalizes the first letter of each word and converts the remaining letters to lowercase.

We can call multiple string methods in a single line by chaining them together. Each method operates on the result returned by the previous method.
For example:
user = user.strip().title()
Here, strip() executes first, and then title() operates on the result.

We can chain as many compatible string methods as we need. However, we must ensure that each method can be applied to the result returned by the previous method.
For example:
user = user.strip().title().split()
This works because strip() and title() return strings, and split() can be applied to the resulting string.

Remember that split() returns a list, not a string. Therefore, we cannot directly call string methods such as capitalize() on the resulting list.

'''


# some more string methods and their oprations:

# capitalize() : It makes the just the first letter of string uppercase.
# title() :  It converts the first letter of each word in a string to uppercase and the remaining letters to lowercase.
# upper() : It converts all the letters in a string to uppercase.
# lower() : It converts all the letters in a string to lowercase.
# lstrip() : It removes spaces from the beginning (left side) of a string.
# rstrip() : It removes spaces from the end (right side) of a string.
# isalpha() : It checks whether all the characters in a string are letters and the string is not empty.
# isdigit() : It checks whether all the characters in a string are digits and the string is not empty.
# isalnum() : It checks whether all the characters in a string are letters or digits and the string is not empty.

