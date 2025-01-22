# In arrays multidimensional arrays are not possible
# In numpy multidimensional arrays are possible

import numpy as np

a = np.array([1,2,3,4.2,5], int)
print(a) # will convert to int

b = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 3x3 matrix

c = np.arange(1,15, 2)
d = np.arange(1,15, 2)
print(c)

# Adds 2 to each element in the array
c = c + 2
print(c)

# Vector addition
e = c + d
print(e)

print(sum(e))
print(min(e))

# Concatenation
f = np.concatenate([c,d])   
print(f)

g = f
# Same id 
print(id(g))
print(id(f))

# Different id
g = f.view()
print(id(g))
print(id(f))
# Theabove is shallow copy
g[0] = 100
print(g)
print(f)

# Deep copy
g = f.copy()
print(id(g))
print(id(f))
g[0] = 400
print(g)
print(f)
