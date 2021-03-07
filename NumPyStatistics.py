# %%
import numpy as np
import matplotlib.pyplot as plt 

# %% Compute the median of the flattened NumPy array
a = np.arange(9)
print(np.median(a))
# %% Find Mean of a List of Numpy Array
a = [   np.array([1, 2, 3]), 
        np.array([4, 5, 6]), 
        np.array([7, 8, 9])]
mean = []
for i in a:
    mean.append(np.mean(i))
print(mean)
# %% Calculate the mean of array ignoring the NaN value
a = [   np.array([1, 2, 3]), 
        np.array([4, np.nan, 6]), 
        np.array([7, 8, 9])]
mean = []
for i in a:
    mean.append(np.nanmean(i))
print(mean)
# %% Get the mean value from given matrix
a = np.matrix(np.arange(9).reshape([3, 3]))
print(a.mean())
# %% Compute the variance of the NumPy array
a = np.arange(9)
print(np.var(a))
# %% Compute the standard deviation of the NumPy array
a = np.arange(9)
print(np.std(a))
# %% Compute pearson product-moment correlation coefficients of two given NumPy arrays
a = np.arange(4)
b = np.array([0, 2, 4, 8])
print(np.corrcoef(a, b))
# %% Calculate the mean across dimension in a 2D NumPy array
a = np.arange(9).reshape([3, 3])
print(np.mean(a, axis=1))
# %%
