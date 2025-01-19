nums = [1,2,3] # list. Can also be different types. Square bracket is list
print(nums)
print(nums[0])
# print(nums[10]) # IndexError: list index out of range
print(nums[2:])
print(nums[-1])
print(nums[-1:]) # Doesn't work as expected
values = [1,2, 'Hrishi', 3.0] # you can have different data
print(values)
print(nums , values) # you can print multiple lists

# List is mutable
nums.append(4) # adds at the end
print(nums)
nums.insert(2, 0) # adds at index 2. Doesn't replace the current value at that index
print(nums)
nums.remove(0) # removes the first occurence of 0
nums.pop(1) # removes the element at index 1
nums.pop() # removes the last element
print(nums)
nums.clear() # removes all elements
# Add and remove multiple elements
nums = [1,2,3,4,5]
del nums[2:] # removes elements from index 2 to end
print(nums)
nums.extend([8,7,6]) # adds elements of the list to the end
print(nums)

# In built functions
print(min(nums))
print(max(nums))
print(sum(nums))
print(nums.index(8)) # returns the index of 8
nums.sort()
print(nums)