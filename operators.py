x = 1
y = 2
z = x/y
print(z) 
print(type(z)) # <class 'float'>
x *= 5
print(x) # 5
x += 5
print(x) # 10
x -= 5
print(x) # 5
a,b = 5,2 # assign multiple values to multiple variables
print(a,b) # 5 2

# Relational operators
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)

# Logical operators. Compares two conditions
# and, or, not
print(a<b and a>b)
print(a<b or a>b)
print(not a<b)
x = 3
y = not x
print(y) # False
