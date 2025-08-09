# Function with parameters and return value
def add_numbers(a, b):
    c = a + b
    return c

# result = add_numbers(1, 2)
# print("Sum: ", result)


# Local Scope
def greet():
    message = "Hello World"
    print(message)
    
# greet()



# Global Scope

greeting = "Hi"

def say_hello():
    print(greeting + " from inside the function")
    
# say_hello()
# print(greeting + " from outside the function")



import math as m
print(m.sqrt(16))
