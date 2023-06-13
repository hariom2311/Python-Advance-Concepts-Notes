# Question 1: Multiply each element in a given list by 2 using list comprehension.

# Solution 1
numbers = [1, 2, 3, 4, 5]
multiplied_numbers = [x * 2 for x in numbers]
print(multiplied_numbers)




# Question 2: Extract all uppercase letters from a string using list comprehension.

# Solution 2
string = "Hello World"
uppercase_letters = [char for char in string if char.isupper()]
print(uppercase_letters)




# Question 3: Remove all duplicates from a given list using list comprehension.

# Solution 3
numbers = [1, 2, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)




# Question 4: Create a list of squares of numbers from 1 to 10 using list comprehension.

# Solution 4
squared_numbers = [x**2 for x in range(1, 11)]
print(squared_numbers)




# Question 5: Filter out all odd numbers from a given list using list comprehension.

# Solution 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
