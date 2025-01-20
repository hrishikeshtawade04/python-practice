# Basic Method

a=  100
b = 31
print(a,b)
temp =  a
a = b
b = temp
print(a,b)

# Math way
a = 100
b = 31
print(a,b)
a = a + b # This is where the addition causes a bigger memory allocation
b = a - b
a = a - b
print(a,b)

# Pythonic way
a = 100
b = 31
print(a,b)
a,b = b,a # b goes to a stack and then a goes to a stack and then it rotates this 2 values. 
# rot_two is what is executed.  

# Logical operator
a = 100
print(bin(a))
b = 31
print(bin(b))
print(a,b)
a = a ^ b # A bigger memory allocation is not required
# 1100100  a
# 0011111  b
# 1111011  a^b
print((0b1111011)) # 123
# 0011111  b
# 1100100  a
b = a ^ b
a = a ^ b
print(a,b)

