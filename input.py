# x = int(input("Enter a number: ")) # input() always returns a string
# y = int(input("Enter another number: ")) # input() always returns a string
# z = x + y # This will concatenate the two strings
# print(z)
# print(type(x))

# How to take only a character
# a = input("Enter a character: ")[0] # This will take only the first character while fetching the input
# print(a)

# Eval
# a = eval(input("Enter an expression:")) # This will evaluate the expression
# print(a)

# Taking arguments
# The 0 argument is the name of the python file
# Hence the first argument is sys.argv[1]
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
print(x+y) # This will add the two arguments
