import numpy as np

# Define the first array 'a'
a = np.array([[10, 4], [8, 12]])

# Define the second array 'b'
b = np.array([[15, 6]])

# Concatenate the arrays 'a' and 'b' along axis 0 (vertically)
c = np.concatenate((a, b), axis=0)

# Print the resulting concatenated array
print(c)
