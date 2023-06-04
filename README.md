# Python Advance Notes
This repository is designed to provide you with comprehensive notes and examples for learning Python Advance programming. Whether you are a beginner getting started with Python or an experienced developer looking to refresh your knowledge, this repository is here to support your learning journey.

# Advance Topic 1: Decorators (decorators-exe.py)
This repository contains code examples showcasing the concept of decorators in Python. Decorators are a powerful feature in Python that allow you to modify the behavior of functions dynamically. They provide a way to wrap a function, modify its functionality, and return the modified function.

## Code Examples

The code examples provided demonstrate various aspects of decorators in Python:

- The first set of examples shows how to define decorators that add additional functionality to functions. It covers scenarios where a decorator is used to add 1 to the result of a function or swap input arguments based on certain conditions.

- The second set of examples illustrates the usage of decorators with functions that accept arbitrary positional and keyword arguments. It demonstrates how decorators can handle different argument types and modify the behavior accordingly.

- The last example showcases the usage of decorators using the `@decorator` syntax, where the decorator is applied directly to the function definition.

## File Structure

- `decorators-exe.py`: This file contains the code examples demonstrating the usage of decorators in Python. Each example is explained using docstrings to provide clarity on the purpose and functionality of the code.



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