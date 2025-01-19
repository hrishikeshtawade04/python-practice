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