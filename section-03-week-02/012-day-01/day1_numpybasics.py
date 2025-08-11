import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
# print(arr)

reshaped = arr.reshape(2, 3)
# print(reshaped[0])
# print(reshaped[1])

zeroes = np.zeros((2, 3))
# print(zeroes)

ones = np.ones((2, 4))
# print(ones)

range_array = np.arange(1, 10, 2)
# print(range_array)

linspace_array = np.linspace(0, 1, 5)
# print(linspace_array)

expanded = arr[:, np.newaxis]
# print(expanded)

arr2 = np.array([1, 2, 3, 4, 5, 6])
# print(arr + arr2)
# print(arr * arr2)
# print(arr / arr2)

# print(np.sqrt(arr))
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
