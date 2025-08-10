squares = [x**2 for x in range(10)]
# print(squares)

evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

# ------------ Lambda Funtions ------------
add = lambda x, y: x + y
# print(add(3, 5))

# ------------ Map ------------
numbers = [1, 2, 3, 4]
sqrs = map(lambda x: x**2, numbers)
# print(list(sqrs))

# ------------ Filter ------------
evenList = filter(lambda x: x % 2 == 0, numbers)
# print(list(evenList))

# ------------ Reduce ------------
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
# print(product)


import os
dir = os.getcwd()
# print(dir)
# os.mkdir("test")
# os.remove("x.txt")

import sys
# print(sys.argv)
# print(sys.version)
