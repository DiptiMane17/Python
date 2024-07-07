import numpy as np

np_array = np.array([1, 2, 3, 4, 5])
print(np_array)
print(np_array[0])
np_array[2] = 10
print(np_array)
np_array = np.append(np_array, 6)
print(np_array)
np_array = np.delete(np_array, 2)
print(np_array)

multi_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(multi_array)
print(multi_array[1, 2])
