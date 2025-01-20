# bitwise operators are used to operate on the bits

# Complement operator (~)
x = 10
print(bin(x)) # 1100
y = ~x # This is 2's complement of x. It is 1's complement of x + 1. 
# in decimal it is -x-1

a = 1
b = 0
print(a & b) # 0 # AND operator
print(a | b) # 1 # OR operator
print(a ^ b) # 1 # XOR operator

# Left shift operator
x = 10
print(x<<2) # 40
# 10 in binary is 1010. Left shift by 2 is 101000 which is 40 in decimal


# Right shift operator
x = 10
print(x>>2) # 2
# 10 in binary is 1010. Right shift by 2 is 10 which is 2 in decimal

