import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

prod = np.matmul(matrix1, matrix2)

transpose = np.transpose(prod)
inverse = np.linalg.inv(prod)

print(prod)
print(transpose)
print(inverse)