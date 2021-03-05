# %%
import numpy as np

N = 3

# %% How to create an empty and a full NumPy array?
a = np.array([])
print(a)
# %% Create a Numpy array filled with all zeros
a = np.zeros(N)
print(a)
# %% Create a Numpy array filled with all ones
a = np.ones(N)
print(a)
# %% Check whether a Numpy array contains a specified row
a = np.array([  [1, 2, 3], 
                [4, 5, 6]])
np.equal(a,[1,2,3]).all(axis=1).any()
np.equal(a,[3,2,1]).all(axis=1).any()
# %% How to Remove rows in Numpy array that contains non-numeric values?
a = np.array([  [1, 2, 3], 
                [4, np.nan, 6],
                [7, 8, 9]])
print(a[~np.isnan(a).any(axis=1)])
# %% Remove single-dimensional entries from the shape of an array
a = np.array([[ [1, 2, 3], 
                [4, 5, 6]]])
print(a.shape)
a = np.squeeze(a)
print(a.shape)
# %% Find the number of occurrences of a sequence in a NumPy array
a = np.array([  [1, 2, 3], 
                [4, 5, 6],
                [2, 3, 4]])
print(repr(a).count("2, 3"))
print(repr(a).count("3, 4"))
# %% Find the most frequent value in a NumPy array
a = np.array([  [1, 2, 3], 
                [4, 4, 6],
                [2, 3, 4]])
print(np.bincount(np.ravel(a)).argmax())
# %% Combining a one and a two-dimensional NumPy Array
a = np.arange(4)
b = np.arange(8).reshape(2,4)
for i, j in np.nditer([a,b]):
    print("%d:%d" % (i,j),)
# %% How to build an array of all combinations of two NumPy arrays?
a = np.array([0, 1])
b = np.array([2, 3])

print(np.array(np.meshgrid(a, b)).T.reshape(-1, 2) )
# %% How to add a border around a NumPy array?
a = np.ones((2, 2))
a = np.pad(a, pad_width=1, mode='constant', 
               constant_values=0)
print(a)
# %% How to compare two NumPy arrays?
a = np.array([0, 1])
b = np.array([2, 3])
c = np.array([2, 3])

print((a == b).all())
print((b == c).all())
# %% How to check whether specified values are present in NumPy array?
a = np.arange(8).reshape(2,4)
4 in a
# %% How to get all 2D diagonals of a 3D NumPy array?
a = np.arange(3 * 4 * 4).reshape(3, 4, 4) 
print(a)
  
diag_a = np.diagonal(a, axis1 = 1, axis2 = 2) 
print(diag_a)
# %% Flatten a Matrix in Python using NumPy
a = np.arange(9).reshape(3,3)
print(a.flatten())
# %% Flatten a 2d numpy array into 1d array
a = np.arange(8).reshape(2,4)
print(a.flatten())
# %% Move axes of an array to new positions
##################################################
#### Dúvida mortal do pq de ter que ser assim:####
##################################################
a = np.zeros((1, 2, 3, 4)) 
print(a)
print(np.moveaxis(a, 1, 2).shape)
# %% Interchange two axes of an array
a = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
print(np.swapaxes(a,0,2))
# %% NumPy – Fibonacci Series using Binet Formula
a = np.arange(1, 11) 
lengthA = len(a) 
# splitting of terms for easiness 
sqrtFive = np.sqrt(5) 
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2
# Implementation of formula 
# np.rint is used for rounding off to integer 
Fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrtFive)) 
print("The first {} numbers of Fibonacci series are {} . ".format(lengthA, Fn))
# %% Counts the number of non-zero values in the array
a = np.array([  [0, 1, 0],
                [1, 0, 1],
                [0, 1, 0]])
print(np.count_nonzero(a))
# %% Count the number of elements along a given axis
a = np.array([  [0, 1, 0],
                [1, 0, 1]])
print(np.size(a, 0))
print(np.size(a, 1))
# %% Trim the leading and/or trailing zeros from a 1-D array
a = np.array([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0])
print(np.trim_zeros(a))
# %% Change data type of given numpy array
a = np.array([  [0, 1, 0],
                [1, 0, 1]])
print(a.astype('float64'))
# %% Reverse a numpy array
a = np.arange(4)
print(np.flip(a))
# %% How to make a NumPy array read-only?
a = np.arange(4)
a.flags.writeable=False
a[1] = 0
# %%
