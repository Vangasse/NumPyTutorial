# %%
import numpy as np
import matplotlib.pyplot as plt 

# %% How to get element-wise true division of an array using Numpy?
a = np.arange(5)
print(np.true_divide(a, 4))
# %% How to calculate the element-wise absolute value of NumPy array?
a = np.array([0, -1, 2, -3])
print(np.absolute(a))
# %% Compute the negative of the NumPy array
a = np.array([0, -1, 2, -3])
print(np.negative(a))
# %% Multiply 2d numpy array corresponding to 1d array
a = np.arange(9).reshape([3, 3])
b = np.arange(3)
print(a * b[:, np.newaxis] )
# %% Computes the inner product of two arrays
a = np.arange(3)
b = np.arange(3)
print(np.dot(a, b))
# %% Compute the nth percentile of the NumPy array
a = np.array([1, 10, 25, 50, 80])
print (np.percentile(a, 25))
print (np.percentile(a, 50))
print (np.percentile(a, 75))
print (np.percentile(a, 100))
# %% Calculate the n-th order discrete difference along the given axis
a = np.array([0, 1, 4, 9, 16])
n = 2
print(np.diff(a, n=n))
# %% Calculate the sum of all columns in a 2D NumPy array
a = np.arange(9).reshape([3, 3])
print(a)
print(np.sum(a, axis=0))
# %% Calculate average values of two given NumPy arrays
a = np.arange(5)
b = np.arange(5)
print((a+b)/2)
# %% How to get the floor, ceiling and truncated values of the elements of a numpy array?
a = np.array([-0.8, -0.1, 0.1, 1.2])
print(np.floor(a))
print(np.ceil(a))
print(np.trunc(a))
# %% How to round elements of the NumPy array to the nearest integer?
a = np.array([-0.8, -0.1, 0.1, 1.2])
print(np.rint(a))
# %% Find the round off the values of the given matrix
a = np.array([-0.8, -0.1, 0.1, 1.2]).reshape([2, 2])
print(np.round(a))
# %% Determine the positive square-root of an array
a = np.array([0, 1, 4, 9, 16])
print(np.sqrt(a))
# %% Evaluate Einstein’s summation convention of two multidimensional NumPy arrays
a = np.array([[1, 2], [0, 2]]) 
b = np.array([[0, 1], [3, 4]]) 
print(np.einsum("mk,kn", a, b))
# %%
