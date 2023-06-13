"""
Dictionary comprehension is a concise and powerful way to create new dictionaries in Python. It allows you to create
a new dictionary by specifying key-value pairs based on an expression, while optionally including conditional statements.
"""

# Example 01: Creating a new dictionary by mapping keys to their corresponding squared values.
original_dict = {'a': 1, 'b': 2, 'c': 3}
squared_dict = {key: value**2 for key, value in original_dict.items()}

print(squared_dict) #output: {'a': 1, 'b': 4, 'c': 9}


# Example 02: Filtering a dictionary to include only key-value pairs with even values.
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_values_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}

print(even_values_dict) #output: {'b': 2, 'd': 4}


# Example 03: Creating a new dictionary by mapping keys to their lengths and assigning -1 for keys with a length greater than 5.
original_dict = {'apple': 5, 'banana': 6, 'cherry': 3, 'kiwi': 4, 'mango': 5, 'papaya': 6}
new_dict = {key: len(key) if len(key) <= 5 else -1 for key in original_dict}

print(new_dict) #output: {'apple': 5, 'banana': -1, 'cherry': -1, 'kiwi': 4, 'mango': 5, 'papaya': -1}


# Example 04: Creating a new dictionary by combining elements from two existing lists.
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
combined_dict = {x: y for x in list1 for y in list2}

print(combined_dict) #output: {'a': 3, 'b': 3, 'c': 3}

