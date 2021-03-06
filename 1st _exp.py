import numpy as np 
arr = np.array( [[ 1, 2, 3], [ 4, 2, 5]] ) # Creating array object 
print("Array is of type: ", type(arr)) # Printing type of arr object 
print("No. of dimensions: ", arr.ndim) # Printing array dimensions (axes) 
print("Shape of array: ", arr.shape) # Printing shape of array 
print("Size of array: ", arr.size) # Printing size (total number of elements) of array 
print("Array stores elements of type: ", arr.dtype) # Printing type of elements in array
c= np.zeros((3, 4)) # Creating a 3X4 array with all zeros 
print ("\nAn array initialized with all zeros:\n", c) 
e = np.random.random((2, 2)) # Create an array with random values 
print ("\nA random array:\n", e) 
f = np.arange(0, 30, 5) # Create a sequence of integers from 0 to 30 with steps of 5 
print ("\nA sequential array with steps of 5:\n", f) 
g = np.linspace(0, 5, 10) # Create a sequence of 10 values in range 0 to 5 
print ("\nA sequential array with 10 values between 0 and 5:\n", g) 
# Reshaping 3X4 array to 2X2X3 array 
arr = np.array([[1, 2, 3, 4],[5, 2, 4, 2],[1, 2, 0, 1]]) 
newarr = arr.reshape(2, 2, 3) 
print ("\nOriginal array:\n", arr) 
print ("Reshaped array:\n", newarr)
# An exemplar array 
arr = np.array([[-1, 2, 0, 4], [4, -0.5, 6, 0], [2.6, 0, 7, 8], [3, -7, 4, 2.0]]) 
# Slicing array 
temp = arr[:2, ::2] 
print ("Array with first 2 rows and alternate columns(0 and 2):\n", temp) 
# Integer array indexing example 
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),(3, 0):\n", temp) 
# boolean array indexing example 
cond = arr > 0 # cond is a boolean array 
temp = arr[cond] 
print ("\nElements greater than 0:\n", temp)