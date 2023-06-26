
from functools import reduce
# 1. What will be the output of this code?

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, map(lambda x: x + 1, numbers)))
print(result)


# a) 120
# b) 48
# c) 60
# d) 240

# What does the following code snippet do?


names = ['Alice', 'Bob', 'Alex', 'Andrew', 'Amy']
result = list(map(lambda x: len(x) > 5, filter(lambda x: x.startswith('A'), names)))

print(result)


# What will be the output of this code?


numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 3, map(lambda x: x * 2, numbers)))
print(result)


# What will be the output of this code?

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, map(lambda x: x * 2, filter(lambda x: x > 2, numbers)), 0)
print(result)

