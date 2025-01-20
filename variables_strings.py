x = 10
y =  9
print(x+y)

# String operations
z = 'Hrishikesh'
print(z[0])
print(z[-1]) # last index
print(z[-2]) # second last index
print(z[0:2]) # 0 to 2 index. Doesnt include 2nd index
print(z[1:]) # 1 to end
print(z[:3]) # start to 2. Doesn't include 3rd index
print(z[3:20]) # 3 to 20. Doesn't include 20th index. Won't throw an error
# z[0] = 'A' # Strings are immutable. This will throw an error
z = 'A' + z[1:] # This is how you can change a string
print(z + " " + str(len(z))) # Length of string


# Advance variable concepts
num = 5 # variable name is num and value is 5. But what is address??
print(id(num)) # Address of variable
num1 = num
print(id(num1)) # address of num 1 is same as num. 
# Both are pointing to same memory location. Address is based the value and not the name you give to the value
# This is memory efficient
num1 = 6 
print(id(num1)) # address of num1 changed. It is now pointing to new memory location
print(num1)
num = 6
print(id(num)) # address of num is same as num1. Both are pointing to same memory location
#so every value has a memory location. If you change the value, it will point to new memory location.
# A variable name tags to the memory location of the value.
# If you change the value, the variable name will point to new memory location
# The old memory location will be garbage collected by python.
# This is how python is memory efficient

# Constants
# Constants are variables whose values cannot be changed.
# In python, we don't have constants. But we can create constants using all caps
PI = 3.14 # So this can be changed. But the intention is to not change it.

# Type of variable
print(type(PI)) # float






