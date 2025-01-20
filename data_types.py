# None = If variable is not assigned any value, it is None
k = None
print(k)

# Numeric = int, float, complex, bool
num = 2.5
print(type(num)) # float
num = 5
print(type(num)) # int
num = 5 + 3j # in python we use j instead of i of complex numbers
print(type(num)) # complex

# Convert type
a = -1
print(int(a)) # converts to int
print(float(a)) # converts to float
print(complex(a)) # converts to complex
print(bool(a)) # converts to bool. True if value is not 0. False if value is 0
c = complex(0, 0)
print(c)
print(c.real) # real part
print(c.imag) # imaginary part
print(bool(c)) # True if real or imaginary part is not 0

# List
lst = [1, 2, 3, 4, 5]
print(type(lst)) # list

# Set
s = {1,2,3,4,5}
print(type(s)) # set

# Tuple
t = (1,2,3,4,5)
print(type(t)) # tuple

# String
s = 'a' # there is no char
print(type(s)) # str
b = "b"
print(type(b)) # str

# Range
a = range(10)
print(type(a)) # range
print(a) # prints range(0, 10)
print(list(a)) # convert range to list and then get the complete list of numbers. 0 to 9. 10 is omitted
print(list(range(0, 11, 2))) #  0 to 10

# Dictionary/Map
d = {1:'a', 2:'b'} # keys do not repeat
print(type(d)) # dict
d = dict({1:'a', 1:'b'})
print(d) # {1: 'b'}. Keys should be unique. If not, the last value will be taken
print(d.keys())
print(d.values())



