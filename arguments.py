
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

# 5. Keyworded variable length arguments
def person(name, **data): # **data is dictionary. Means multiple values for a specific key
    print(name)
    for key, value in data.items(): # you can also call **data as **kwargs
        print(key, value)

person('John', age=30, city='New York', phone=1234567890)
person('John', age=30, place='New York')
