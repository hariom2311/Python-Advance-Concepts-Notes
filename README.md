# Python Advance Notes
This repository is designed to provide you with comprehensive notes and examples for learning Python Advance programming. Whether you are a beginner getting started with Python or an experienced developer looking to refresh your knowledge, this repository is here to support your learning journey.


# Steps To Clone Repository

### Windows/Ubuntu

1. Open the command prompt or Git Bash on your Windows machine.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository: 
```
git clone https://github.com/hariom2311/Python-Advance-Concepts-Notes.git
```

## Pull Updates

To get the latest updates from the remote repository, you can follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the cloned repository directory.
3. Run the following command to pull the updates:
```
git pull origin master
```


# Advance Topic 1: Decorators (decorators-exe.py)
This repository contains code examples showcasing the concept of decorators in Python. Decorators are a powerful feature in Python that allow you to modify the behavior of functions dynamically. They provide a way to wrap a function, modify its functionality, and return the modified function.

## Code Examples

The code examples provided demonstrate various aspects of decorators in Python:

- The first set of examples shows how to define decorators that add additional functionality to functions. It covers scenarios where a decorator is used to add 1 to the result of a function or swap input arguments based on certain conditions.

- The second set of examples illustrates the usage of decorators with functions that accept arbitrary positional and keyword arguments. It demonstrates how decorators can handle different argument types and modify the behavior accordingly.

- The last example showcases the usage of decorators using the `@decorator` syntax, where the decorator is applied directly to the function definition.

## File Structure

- `decorators-exe.py`: This file contains the code examples demonstrating the usage of decorators in Python. Each example is explained using docstrings to provide clarity on the purpose and functionality of the code.

## Learning Material
- Video Tutorial: https://youtu.be/MSDKKS9S3z0
- Video Tutorial Notes: https://docs.google.com/document/d/1rmUJ5FCDUdPH_SCAl3aGIeoecQ2dAvUOUfpRYaeGlbw/edit?usp=sharing
- Video Tutorial Codes: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/notes
- Practice Exercise Questions: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/exercise_questions 
- Practice Exercise Questions Solutions: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/exercise_solutions




# Advance Topic 2: Python Lambda, Map, Filter, and Reduce (lambda_map_filter_reduce.py)

This repository contains code examples showcasing the usage of lambda functions, `map()`, `filter()`, and `reduce()` in Python. These functional programming constructs provide concise and powerful ways to manipulate data and perform common operations.

## Lambda

The code demonstrates the usage of lambda functions in Python:

- The `mul` function is a normal function that multiplies two numbers.
- The `x` variable is a lambda function that does the same multiplication.
- The output is printed for both the normal function and the lambda function.

## Map

The code shows examples of using the `map()` function in Python:

- First, a list of strings `my_pets` is transformed to uppercase using a for loop.
- Then, the same transformation is achieved using the `map()` function with `str.upper`.
- Lastly, a lambda function is used with `map()` to uppercase the strings in `my_pets`.
- The outputs of each transformation are printed.

## Filter

The code demonstrates the usage of the `filter()` function in Python:

- A list of scores is filtered to include only scores greater than 75 using a defined function.
- The same filtering is done using a lambda function with `filter()`.
- The filtered scores are printed as the output.

## Reduce

The code shows examples of using the `reduce()` function in Python:

- First, a list of numbers is reduced by adding them together using a defined function.
- The same reduction is achieved using `reduce()` with a lambda function for addition.
- The result of the reduction is printed as the output.
- Another example demonstrates the usage of `reduce()` with an initial value provided.
- The numbers are again reduced by addition, starting from 10.
- The result of the reduction is printed as the output.

## File Structure

- `lambda_map_filter_reduce.py`: This file contains the code examples demonstrating the usage of lambda functions, `map()`, `filter()`, and `reduce()` in Python. Each example is explained using comments to provide clarity on the purpose and functionality of the code.

## Learning Material
- Video Tutorial: https://youtu.be/qp_udoVOlL8
- Video Tutorial Notes: https://docs.google.com/document/d/1WnJhwCVrlgE9K2pjEAEEZbDxe_cKm3LLGeBvH2U6hZQ/edit?usp=sharing
- Video Tutorial Codes: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/notes
- Practice Exercise Questions: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/exercise_questions 
- Practice Exercise Questions Solutions: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/exercise_solutions

# Advance Topic 3 Part-1: Python Collections - ChainMap and Counter

This repository contains code examples showcasing the usage of `collections.ChainMap` and `collections.Counter` in Python. These features provide convenient ways to handle multiple mappings and perform counting operations.

## ChainMap

The code demonstrates the usage of the ChainMap class in Python:

## Merging Multiple Dictionaries

- Two dictionaries, dict1 and dict2, are defined.
- The dictionaries are combined into a single chain_map using ChainMap(dict1, dict2).
- The combined chain_map behaves as a single dictionary that retains the original mappings.
- The output demonstrates accessing values from the chain_map using both individual dictionaries and the chain_map itself.

## Updating Values

- Two dictionaries, dict1 and dict2, are defined.
- A chain_map is created using ChainMap(dict1, dict2).
- Values in the chain_map are updated using the update() method.
- The updated values are accessed from the chain_map.
- Example 3: Reordering the ChainMap

## Two dictionaries, dict1 and dict2, are defined.
- A chain_map is created using ChainMap(dict1, dict2).
- The new_child() method is used to reorder the chain_map.
- The output demonstrates accessing values from the reordered chain_map.

## Accessing Keys and Values Iteratively

- Two dictionaries, dict1 and dict2, are defined.
- A chain_map is created using ChainMap(dict1, dict2).
- The items() method is used to iterate over the keys and values of the chain_map.
- The keys and values are printed as output.
## Counter
The code demonstrates the usage of the Counter class in Python:

## Counting Elements in a List

- A list of elements, my_list, is defined.
- A counter object is created using Counter(my_list).
- The counts of each element in the counter are accessed using indexing.
- The counts are printed as output.

## Counting Characters in a String

- A string, my_string, is defined.
- A counter object is created using Counter(my_string).
- The counts of each character in the counter are accessed using indexing.
- The counts are printed as output.

## Counting Words in a Sentence

- A sentence, my_sentence, is defined.
- A counter object is created using Counter(my_sentence.split()).
- The counts of each word in the counter are accessed using indexing.
- The counts are printed as output.

## Common Patterns and Operations with Counter

- A counter object is created using Counter('abracadabra').
- Common patterns and operations with counter are demonstrated, including most_common(), arithmetic operations, and updating counts.
- The results are printed as output.


## File Structure

- `notes\collection_module\chainmap_notes.py` and `notes\collection_module\counter_notes.py`: This file contains the code examples demonstrating the usage of `counter` module, `ChainMap()` and `Counter()` in Python. Each example is explained using comments to provide clarity on the purpose and functionality of the code.

## Learning Material
- Video Tutorial: https://youtu.be/Bh1_-xNGsbU
- Video Tutorial Notes: https://docs.google.com/document/d/1XI7FlLKGyDLWpsTK2DOWUgIZ3HGeSmlLDb2oZBymYBw/edit?usp=sharing
- Video Tutorial Codes: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/notes/collection_module
- Practice Exercise Questions: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/exercise_questions/collection_exercise_questions 
- Practice Exercise Questions Solutions: https://github.com/hariom2311/Python-Advance-Concepts-Notes/tree/master/exercise_solutions/collection_exercise_solution
