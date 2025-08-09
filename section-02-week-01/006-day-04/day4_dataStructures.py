# ------------- Lists -------------
numbers = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True]
# print("------- Fruits -------")
# print(fruits)

# print(numbers[2])
# print(fruits[-1])
# print(mixed[1])

fruits.append("orange")
# print("------- Add Orange -------")
# print(fruits)

fruits.insert(1, "grape")
# print("------- Add Grape -------")
# print(fruits)

sliced_fruits = fruits[2:4]
# print("------- Slice 2:4 -------")
# print(sliced_fruits)

fruits.remove("banana")
# print("------- Remove Banana -------")
# print(fruits)

del fruits[0]
# print("------- Remove First Fruit -------")
# print(fruits)

fruits.pop()
# print("------- Remove Last Fruit -------")
# print(fruits)



# ------------- Tuples -------------
colors = ("red", "green", "blue")
single_item = ("glass",)

# print(colors[0])
# print(colors[-1])


# ------------- Dictionaries -------------
student = {"name": "Alice", "age": 25, "grade": "A"}

# for key, value in student.items():
#     print(key, value)


student["subject"] = "Math"
student["age"] = 32
# print(student)

del student["grade"]
# print(student)


student.pop("subject")
# print(student)

# ------------- Sets -------------
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 - set2)
print(set1 & set2)
print(set1 | set2)
