# %%
import numpy as np
import matplotlib.pyplot as plt 

# %% Create a Numpy array with random values
a = np.empty([4, 4], dtype=int)
print(a)
# %% How to choose elements from the list with different probability using NumPy?
a = np.arange(9)
print(np.random.choice(a))
# %% How to get weighted random choice in Python?
a = np.arange(9)
print(np.random.choice(a, 1, p=[0.05, 0.05, 0.05, 0.2, 0.3, 0.2, 0.05, 0.05, 0.05]))
# %% Generate Random Numbers From The Uniform Distribution using NumPy
a = np.random.uniform(size=1000)
count, bins, ignored = plt.hist(a, 40, density = True) 
plt.show()
# %% Get Random Elements form geometric distribution
a = np.random.geometric(0.5, 1000)
count, bins, ignored = plt.hist(a, 40, density = True) 
plt.show()
# %% Get Random elements from Laplace distribution
a = np.random.laplace(0, 1, 1000)
count, bins, ignored = plt.hist(a, 40, density = True) 
plt.show()
# %% Return a Matrix of random values from a uniform distribution
a = np.random.uniform(size=100).reshape([10, 10])
count, bins, ignored = plt.hist(a, 40, density = True) 
plt.show()
# %% Return a Matrix of random values from a Gaussian distribution
a = np.random.normal(size=10000).reshape([100, 100])
count, bins, ignored = plt.hist(a) 
plt.show()
# %% 
