# %%
import numpy as np

# %% Get the maximum value from given matrix
a = np.matrix('[0, 1; 2, 3]')
print(a.max())
# %% Get the minimum value from given matrix
a = np.matrix('[0, 1; 2, 3]')
print(a.min())
# %% Find the number of rows and columns of a given matrix using NumPy
a = np.matrix('[0, 1; 2, 3]')
print(a.shape)
# %% Select the elements from a given matrix
a = np.matrix('[0, 1; 2, 3]')
print(a[0,0])
# %% Find the sum of values in a matrix
a = np.matrix('[0, 1; 2, 3]')
print(np.sum(a))
# %% Calculate the sum of the diagonal elements of a NumPy array
a = np.matrix('[0, 1; 2, 3]')
print(np.trace(a))
# %% Adding and Subtracting Matrices in Python
a = np.matrix('[0, 1; 2, 3]')
b = np.matrix('[0, 0; 1, 2]')
print(a+b)
print(a-b)
# %% Ways to add row/columns in numpy array
a = np.matrix('[0, 1; 1, 1]')
add = np.array([[2, 2]])
print(np.vstack((a, add)))
print(np.hstack((a, add.T)))
# %% Matrix Multiplication in NumPy
a = np.matrix('[1, 1; 1, 1]')
b = np.matrix('[2, 2; 2, 2]')
print(np.dot(a,b))
# %% Get the eigenvalues of a matrix
a = np.matrix('[1, 1; 1, 1]')
print(np.linalg.eig(a)[0])
# %% How to Calculate the determinant of a matrix using NumPy?
a = np.matrix('[0, 1; 2, 3]')
print(np.linalg.det(a))
# %% How to inverse a matrix using NumPy
a = np.matrix('[0, 1; 2, 3]')
print(np.linalg.inv(a))
# %% Convert the matrix into a list
a = np.matrix('[0, 1; 2, 3]')
print(a.tolist())
# %%
