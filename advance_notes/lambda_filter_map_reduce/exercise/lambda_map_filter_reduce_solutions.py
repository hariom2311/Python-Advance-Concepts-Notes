
"""
Question 1
Write a program to filter out the even numbers from a given list using the filter function and a lambda function.
"""
# Solution 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# ====================================================================================

"""
Question 2
Write a program to square all elements in a given list using the map function and a lambda function.
"""

# Solution 2
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# ====================================================================================\

"""
Question 3
Write a program to calculate the sum of all numbers in a given list using the reduce function and a lambda function.
"""

# Solution 3

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)
