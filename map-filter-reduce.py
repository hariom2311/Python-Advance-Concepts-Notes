"""
Lambda:
- The code demonstrates the usage of lambda functions in Python.
- The `mul` function is a normal function that multiplies two numbers.
- The `x` variable is a lambda function that does the same multiplication.
- The output is printed for both the normal function and the lambda function.
"""

# this is normal function
def mul(a, b):
    return a*b
print(mul(5, 6))


# this is lambda function
x = lambda a, b : a * b
print(x(5, 6))

"""
Map:
- The code shows examples of using the `map()` function in Python.
- First, a list of strings `my_pets` is transformed to uppercase using a for loop.
- Then, the same transformation is achieved using the `map()` function with `str.upper`.
- Lastly, a lambda function is used with `map()` to uppercase the strings in `my_pets`.
- The outputs of each transformation are printed.
"""
# without map() method
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

# Using map() method
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# Using map() method with lambda function
my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(lambda string: string.upper(), my_pets))

print(uppered_pets)


# another example of map() with 2 iterables
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 7)))

print(result)


"""
Filter:
- The code demonstrates the usage of the `filter()` function in Python.
- A list of scores is filtered to include only scores greater than 75 using a defined function.
- The same filtering is done using a lambda function with `filter()`.
- The filtered scores are printed as the output.
"""
#filter method

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

# filter() method with lambda function
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

"""
Reduce:
- The code shows examples of using the `reduce()` function in Python.
- First, a list of numbers is reduced by adding them together using a defined function.
- The same reduction is achieved using `reduce()` with a lambda function for addition.
- The result of the reduction is printed as the output.
- Another example demonstrates the usage of `reduce()` with an initial value provided.
- The numbers are again reduced by addition, starting from 10.
- The result of the reduction is printed as the output.
"""
# example of reduce()
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)

# example of reduce() with 3 arguments
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers, 10)
print(result)
