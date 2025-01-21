# Have values with same type. Unlike list or tuple
# You can easily appened and remove elements

from array import array

# char has 1 byte
# int has 2 bytes. short int has 2 bytes. long int has 4 bytes
# float has 4 bytes
# double has 8 bytes
# will throw an error if u try float
vals = array('i', [5, 9, 8, 4, 2]) # i is the type code for integer
print(vals)
print(vals.buffer_info()) # (address, size)
print(vals.typecode) # print i as type code
vals.reverse()
print(vals)
vals.append(1)
print(vals)
# vals.remove(10) # will throw an error if element is not present
# print(vals)
print(vals[4])
for i in vals:
    print(i, end=" ")
print()
# create new array with same values
newArr = array(vals.typecode, vals)
print(newArr)
newArr = array(vals.typecode, (a for a in vals)) # works the same as above
print(newArr)
squarredArr = array(vals.typecode, (a*a for a in vals))
print(squarredArr)

# create array from user input
arr = array('i', [])
n = int(input("Enter the length of array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr.index(8)) # will return the index of the element the first time it occurs. Otherwise will throw an error