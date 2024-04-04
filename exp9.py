import numpy as np

# Creating an array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Displaying the original array
print("Original Array:")
print(arr)

# Accessing elements of the array
print("\nAccessing elements:")
print("Element at (0, 0):", arr[0, 0])
print("Element at (1, 2):", arr[1, 2])

# Slicing the array
print("\nSliced Array:")
print("First row:", arr[0])
print("First column:", arr[:, 0])
print("Subarray from index (0, 1) to (1, 2):")
print(arr[0:2, 1:])

# Modifying elements of the array
arr[0, 0] = 10
arr[1, 2] = 20
print("\nModified Array:")
print(arr)

# Performing arithmetic operations on arrays
print("\nArray Operations:")
arr2 = np.array([[2, 3, 4],
                 [5, 6, 7],
                 [8, 9, 10]])
print("Addition:")
print(arr + arr2)
print("Multiplication:")
print(arr * arr2)

# Using NumPy functions
print("\nNumPy Functions:")
print("Sum of all elements in the array:", np.sum(arr))
print("Minimum value in the array:", np.min(arr))
print("Maximum value in the array:", np.max(arr))
print("Mean of the array:", np.mean(arr))
