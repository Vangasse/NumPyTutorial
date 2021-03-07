# %%
import numpy as np
from numpy.polynomial.polynomial import polygrid2d
from numpy.polynomial.polynomial import polygrid3d 

# %% Define a polynomial function
a = np.poly1d([1, 0, 2, 10])
print(a)
# %% How to add one polynomial to another using NumPy in Python?
a = np.poly1d([1, 0, 1, 0])
b = np.poly1d([1, 0, 1])
print(np.polyadd(a, b))
# %% How to subtract one polynomial to another using NumPy in Python?
a = np.poly1d([1, 0, 1, 0])
b = np.poly1d([1, 0, 1])
print(np.polysub(a, b))
# %% How to multiply a polynomial to another using NumPy in Python?
a = np.poly1d([1, 0, 1, 0])
b = np.poly1d([1, 0, 1])
print(np.polymul(a, b))
# %% How to divide a polynomial to another using NumPy in Python?
a = np.poly1d([1, 0, 1, 0])
b = np.poly1d([1, 0])
print(np.polydiv(a, b))
# %% Find the roots of the polynomials using NumPy
a = np.poly1d([1, 0, 1, 0])
print(np.roots(a))
# %% Evaluate a 2-D polynomial series on the Cartesian product
a = np.array([[1, 3, 5], [2, 4, 6]])
print(polygrid2d([7, 9], [8, 10], a))
# %% Evaluate a 3-D polynomial series on the Cartesian product
a = np.array([[1, 3, 5], [2, 4, 6], [10, 11, 12]])
print(polygrid3d([7, 9], [8, 10], [5, 6], a))
# %%
