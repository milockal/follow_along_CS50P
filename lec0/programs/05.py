
#Some Programs using "int()" ; a built in fn in python to define integers

#adding two integers

x =(int (input("Enter the first number ")))
y =(int (input("Enter the second number ")))

z = (x+y)
print(fr"result = {z} ")


# You can use int fn to make sure the input is considered as integer otherwise it will get considered as string and on string a "+" sign acts as concatenation rather than addition
# To perform any mathematical operations we needa make sure that the passed value is not considered as str. so, if we simply take input without particularly defining it as mathematical number it will get considered as str
# To convert inputted value from str to int or anything else we use type conversion. input = 1 is a str but input(int()) makes sure inputted value is considered as numeric value rather than str
# You can assign a numeric value directly to a variable as well and it will get considered as numrical value unless you put that inside quotation marks. e.g x = 1 is int whereas x = "1" is str


