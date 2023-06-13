# Question 1: Create a dictionary with the squares of numbers from 1 to 5.

# Soution 1
squared_numbers = {x: x**2 for x in range(1, 6)}
print(squared_numbers)



# Question 2: Convert a list of strings into a dictionary with string lengths as keys.

# Solution 2
strings = ['apple', 'banana', 'cherry']
string_lengths = {s: len(s) for s in strings}
print(string_lengths)



# Question 3: Filter out key-value pairs from a dictionary based on a condition.

# Solution 3
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
filtered_numbers = {k: v for k, v in numbers.items() if v > 2}
print(filtered_numbers)



# Question 4: Create a dictionary from two lists using list comprehension.

# Solution 4
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print(combined_dict)



# Question 5: Convert a dictionary of names and ages into a dictionary of ages and names.

# Solution 5
names_ages = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
ages_names = {v: k for k, v in names_ages.items()}
print(ages_names)
