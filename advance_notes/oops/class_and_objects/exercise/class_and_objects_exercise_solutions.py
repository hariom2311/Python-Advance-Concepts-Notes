import math

# Question 1: Create a class Person with attributes name and age. Implement a method introduce() that prints a greeting message with the person's name and age.

# Solution 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person = Person("Alice", 25)
person.introduce()


# Question 2: Create a class BankAccount with attributes account_number and balance. Implement methods deposit(amount) and withdraw(amount) to update the account balance.

# Solution 2
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")


account = BankAccount("123456789", 1000)
print(account.balance)     # Output: 1000

account.deposit(500)
print(account.balance)     # Output: 1500

account.withdraw(200)
print(account.balance)     # Output: 1300

account.withdraw(2000)     # Output: Insufficient funds.


# Question 3: Create a class Employee with attributes name and salary. Implement a method get_raise(percentage) that increases the employee's salary by the given percentage.

# Solution 3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_raise(self, percentage):
        self.salary *= (1 + percentage / 100)


employee = Employee("John Doe", 5000)
print(employee.salary)    # Output: 5000

employee.get_raise(10)
print(employee.salary)    # Output: 5500

employee.get_raise(5)
print(employee.salary)    # Output: 5775


# Question 4: Create a class Point with attributes x and y representing coordinates. Implement a method distance_from_origin() that calculates and returns the distance of the point from the origin (0, 0).

# Solution 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


point = Point(3, 4)
print(point.distance_from_origin())    # Output: 5.0


# Question 5: Create a class Book with attributes title and author. Implement a method display() that prints the book's title and author.

# Solution 5
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


book = Book("Harry Potter", "J.K. Rowling")
book.display()
