"""
Numpy
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

arr = np.array((1, 2, 3, 4, 5))

print(arr)


import numpy as np

print(np.__version__)


#%% Create a 0-D array with value 42
arr0D = np.array(42)
print(arr0D)


#%% Create a 1-D array containing the values 1,2,3,4,5:
arr1D = np.array([1, 2, 3, 4, 5])
print(arr1D)

#%% Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)

#%% Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3D)

print(arr0D.ndim)
print(arr1D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)