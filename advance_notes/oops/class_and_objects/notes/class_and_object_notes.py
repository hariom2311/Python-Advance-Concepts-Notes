"""
In Python, a class is a blueprint or a template for creating objects. It defines the characteristics (attributes) 
and behaviors (methods) that the objects of that class will have. It provides a way to organize and structure code 
by grouping related data and functions together.

An object, on the other hand, is an instance of a class. It represents a specific entity or instance that can have 
its own unique state and behavior. When you create an object, you are creating a specific instance based on the class
 definition.
"""

# Here's an example that demonstrates the concept of a class and object in Python:

# Define a class named "Person"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Create an object of the Person class
person = Person("Alice", 25)

# Access object attributes
print(person.name)  # Output: Alice
print(person.age)   # Output: 25

# Call object methods
person.greet()  # Output: Hello, my name is Alice and I am 25 years old.

# Let'st take another example


# Define a class named "Rectangle"
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an object of the Rectangle class
my_rectangle = Rectangle(5, 3)

# Access object attributes
print(my_rectangle.width)  # Output: 5
print(my_rectangle.height)  # Output: 3

# Call object methods
print(my_rectangle.area())  # Output: 15
print(my_rectangle.perimeter())  # Output: 16
