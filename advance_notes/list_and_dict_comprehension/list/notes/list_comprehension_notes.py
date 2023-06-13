"""
List comprehension is a concise and powerful way to create new lists in Python. It allows you to create a new list by
applying an expression to each element of an existing iterable (such as a list, tuple, or range), while also providing
the option to include conditional statements.
"""


# Example 01: Creating a new list with the square of each element in an existing list.
original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list]

print(squared_list) #output: [1, 4, 9, 16, 25]




# Example 02: Filtering a list to include only even numbers.
original_list = [1, 2, 3, 4, 5]
even_numbers = [x for x in original_list if x % 2 == 0]

print(even_numbers) #output: [2, 4]



# Example 03: Creating a new list with squared values for even numbers and -1 for odd numbers.
original_list = [1, 2, 3, 4, 5]
new_list = [x**2 if x % 2 == 0 else -1 for x in original_list]

print(new_list) #output: [-1, 4, -1, 16, -1]



# Example 04: Creating a new list by combining elements from two existing lists.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = [(x, y) for x in list1 for y in list2] 
#output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]