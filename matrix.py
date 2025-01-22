import numpy as np

mat = np.array( [
    [1, 2, 3, 4],
    [4, 5, 6, 4]
            ])

# Type of data
print(mat.dtype)

# Number of dimensions
print(mat.ndim) # Number of dimensions nxm

# Shape of the matrix
print(mat.shape) # row, col

# Size
print(mat.size) # Number of elements

# Multidimensional to 1D
flatmat = mat.flatten()
print(flatmat)
print(flatmat.shape)
print(flatmat.dtype)

# 1D to multidimensional
mat2 = flatmat.reshape(4, 2) # 4 rows, 2 columns
print(mat2)

mat3 = flatmat.reshape(2, 2, 2) # 2 X 2 X 2
print(mat3)
print(mat3.ndim)

# Matrix format
m = np.matrix(mat)
print(m)
m1 = np.matrix('1 2; 3 4')
print(m1)

# Diagonal matrix
d = np.diag(m1)
print(d)
print(m1.min())

# Matrix multiplication
m2 = np.matrix('1 2; 3 4')
m3 = np.matrix('5 6; 7 8')
print(m2 * m3)

# Matrix addition
print(m2 + m3)



