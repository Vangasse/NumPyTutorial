import numpy as np

# %% Replace NumPy array elements that doesn’t satisfy the given condition
a = np.array([1, 10, 5, 7, 3])
print(a[a>5])
a[a>5] = 1
print(a)
# %% Return the indices of elements where the given condition is satisfied
a = np.array([1, 10, 5, 7, 3])
print(np.where(a>5))
# %% Replace NaN values with average of columns
a = np.array([  [6, 7,      np.nan],
                [1, np.nan, 9],
                [8, 3,      4]])
col_mean = np.nanmean(a, axis = 0)
inds = np.where(np.isnan(a)) 
a[inds] = np.take(col_mean, inds[1]) 
print(a)
# %% Replace negative value with zero in numpy array
a = np.array([1, -10, 5, -7, 3])
a[a<0] = 0
print(a)
# %% How to get values of an NumPy array at certain index positions?
a = np.arange(4)
b = np.zeros(2)
a.put([1,3], b)
print(a)
# %% Find indices of elements equal to zero in a NumPy array
a = np.array([0, 1, 1, 0, 1, 0])
print(np.where(a==0))
# %% How to Remove columns in Numpy array that contains non-numeric values?
a = np.array([  [1, 2, 3], 
                [4, np.nan, 6],
                [7, 8, 9]])
print(a[:, ~np.isnan(a).any(axis=1)])
# %% How to access different rows of a multidimensional NumPy array?
a = np.array([  [1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9]])
print(a[0:2])
print(a[[0,2]])
# %% Get row numbers of NumPy array having element larger than X
a = np.array([  [6, 7, 2],
                [1, 5, 9],
                [8, 3, 4]])
print(np.where(np.any(a > 7, axis = 1)))
# %% Get filled the diagonals of NumPy array
a = np.zeros(9).reshape((3,3))
np.fill_diagonal(a, 1)
print(a)
# %% Check elements present in the NumPy array
a = np.arange(8).reshape(2,4)
4 in a
# %% Combined array index by index
a = np.arange(4)
b = np.arange(4)
c = np.array([])
for i in range(len(b)):
    c = np.hstack((c, a[i]))
    c = np.hstack((c, b[i]))
print(c)
# %%
