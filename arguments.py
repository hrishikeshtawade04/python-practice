
# a,b are formal arguments
def add(a, b):
    return a + b

# 1, 2 are actual arguments
add(1, 2)

# 4 types of actual arguments
# 1. Positional arguments: Order of arguments is important
def person(name, age):
    print(name, age)

person('John', 30) # We can't change the order of arguments

# 2. Keyword arguments
person(age=30, name='John') # We can change the order of arguments

# 3. Default arguments
def person(name, age=18): # Default value of age is 18
    print(name, age)

person(name='John') # age will be 18

# 4. Variable length arguments
def sum(a=0, *b): # *b is tuple. Means multiple values
    c = a
    for i in b:
        c += i
    print(c)

sum(5,6,7) 
sum()

