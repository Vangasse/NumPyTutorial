# %%
import numpy as np
import matplotlib.pyplot as plt 

# %% How to get the indices of the sorted array using NumPy in Python?
a = np.array([2, 4, 8, 6, 1, 9, 5, 3, 7])
print(np.argsort(a))
# %% Finding the k smallest values of a NumPy array
a = np.array([2, 4, 8, 6, 1, 9, 5, 3, 7])
k = 3
print(np.sort(a)[:k])
# %% How to get the n-largest values of an array using NumPy?
a = np.array([2, 4, 8, 6, 1, 9, 5, 3, 7])
k = 3
print(np.sort(a)[-k:])
# %% Sort the values in a matrix
a = np.array([2, 4, 8, 6, 1, 9, 5, 3, 7]).reshape([3, 3])
print(a)
a = np.sort(np.ravel(a)).reshape([3, 3])
print(a)
# %% Filter out integers from float numpy array
a = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
print(a[a != a.astype(int)] )
# %% 