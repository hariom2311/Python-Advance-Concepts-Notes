
"""
Question 1
Write a decorator function timer that measures the execution time of any function and prints the elapsed time.
"""
# Solution 1

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        return result
    return wrapper

@timer
def my_function():
    time.sleep(2)

my_function()
# ====================================================================================

"""
Question 2
Create a decorator function debug that prints the arguments and return value of any function when it is called.
"""

# Solution 2

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(3, 5)

# ====================================================================================\

"""
Question 3
Implement a decorator function cache that caches the return value of any function for future calls with the same arguments.
"""

# Solution 3

def cache(func):
    memo = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in memo:
            memo[key] = func(*args, **kwargs)
        return memo[key]

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(15))

# ====================================================================================

"""
Question 4
Write a decorator function log_exceptions that catches any exceptions raised by a function and logs them.
"""
# Solution 4

import logging

def log_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(f"Exception in function {func.__name__}: {str(e)}")
    return wrapper

@log_exceptions
def divide(a, b):
    return a / b

divide(10, 0)
