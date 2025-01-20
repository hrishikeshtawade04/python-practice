# Every key will have a value assigned to it. Mutable data type

data = {1:'Hrishikesh', 2:'Rajesh', 3:'Rahul', 4:'Rohit'}
print(data[1]) # Specify key to get value
# print(data[20]) # KeyError: 20
print(data.get(20)) # None
print(data.get(20, 'Not Found')) # Get method to avoid KeyError

# Creating dictionary using two lists
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
data = dict(zip(keys, values))
print(data)
data1 = dict({1:'Hrishikesh', 2:'Rajesh', 3:'Rahul', 4:'Rohit'})
print(data1)
data1.update({4:'Rohan'})
print(data1)
del data1[4] # Delete key
print(data1)
