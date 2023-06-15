"""
generators provide a powerful and flexible tool for handling data sequences, enabling memory-efficient and
computationally efficient processing, simplified code structure, and support for infinite or large-scale data streams.
"""



# Generating a Sequence of Numbers:
def number_generator(n):
    for i in range(n):
        yield i

# Usage:
gen = number_generator(5)
for num in gen:
    print(num)

"""
The number_generator function uses the yield keyword to create a generator that generates a sequence of numbers
from 0 to n-1. Each number is yielded one at a time when the generator is iterated over.
"""





# Lazy Evaluation:
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage:
gen = fibonacci_generator()
for _ in range(10):
    print(next(gen))

"""
The fibonacci_generator function creates an infinite generator that generates Fibonacci numbers.
The generator uses lazy evaluation, computing and yielding the next Fibonacci number only when requested using the next
function.
"""




# Filtering Elements:
def even_numbers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Usage:
gen = even_numbers_generator(10)
for num in gen:
    print(num)

"""
The even_numbers_generator function generates even numbers up to n-1.
It filters out odd numbers by using an if statement within the generator function.
"""



# Infinite Stream of Data:
def infinite_stream_generator():
    i = 0
    while True:
        yield i
        i += 1

# Usage:
gen = infinite_stream_generator()
for _ in range(10):
    print(next(gen))

"""
The infinite_stream_generator function generates an infinite stream of numbers starting from 0.
It keeps incrementing the value of i and yields it indefinitely.
"""