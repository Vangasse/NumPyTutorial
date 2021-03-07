# %%
import numpy as np

# %% Find a matrix or vector norm using NumPy
a = np.arange(9).reshape(3,3)
print(np.linalg.norm(a))
# %% Calculate the QR decomposition of a given matrix using NumPy
a = np.arange(9).reshape(3,3)
q, r = np.linalg.qr(a)
print(q)
print(r)
# %% Compute the condition number of a given matrix using NumPy
a = np.arange(9).reshape(3,3)
print(np.linalg.cond(a))
# %% Compute the eigenvalues and right eigenvectors of a given square array using NumPy?
a = np.arange(9).reshape(3,3)
print(np.linalg.eig(a))
# %% Calculate the Euclidean distance using NumPy
a = np.array((1, 2, 3)) 
b = np.array((1, 1, 1))
print(np.linalg.norm(a - b))
# %%
