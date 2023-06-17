# Question 1: Create a generator function countdown(n) that counts down from n to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)    # Output: 5 4 3 2 1 0


# Question 2: Create a generator function fibonacci(n) that generates the first n Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(8):
    print(num)    # Output: 0 1 1 2 3 5 8 13


# Question 3: Create a generator function odd_numbers(n) that generates the first n odd numbers.
def odd_numbers(n):
    count = 0
    num = 1
    while count < n:
        yield num
        num += 2
        count += 1

for num in odd_numbers(6):
    print(num)    # Output: 1 3 5 7 9 11
