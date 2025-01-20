# Tuple is immutable, but we can change the value of tuple by converting it to list and then back to tuple.
# Iteration in tuple is faster than list
# Tuple is used when you want to make sure that the data is not changed

tuple1 = (1,2,3) # round bracket is tuple
print(tuple1[1])
# tuple1[1] = 5

# Set. It is unordered and doesn't have duplicates. Mutable. Doesn't support indexing
s = {1,2,3,4,4}
print(s) # removes duplicates and doesn't maintain order. Reason is that set is implemented using hash table
# print(s[0]) # TypeError: 'set' object is not subscriptable
s.add(5) # adds 5
print(s)
s.update([6,7,8]) # adds multiple elements
print(s)