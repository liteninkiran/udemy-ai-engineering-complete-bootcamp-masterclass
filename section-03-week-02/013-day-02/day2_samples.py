import numpy as np

# Scalar Broadcasting
arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr + 10)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
# print(matrix + vector)
# print(matrix * vector)

# print("Sum: ", np.sum(matrix))
# print("Mean: ", np.mean(matrix))
# print("Min: ", np.min(matrix))
# print("Max: ", np.max(matrix))
# print("St Dev: ", np.std(matrix))
# print("Sum Rows: ", np.sum(matrix, axis = 1))
# print("Sum Cols: ", np.sum(matrix, axis = 0))

evens = arr[arr % 2 == 0]
# print(evens)

arr[arr > 3] = 0
# print(arr)


np.random.seed(42)

random_array = np.random.rand(3, 3)
# print("Random Array: \n", random_array)

random_integers = np.random.randint(0, 10, size=(2,3))
# print("Random Integers: \n", random_integers)
