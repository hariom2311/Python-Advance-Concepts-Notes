"""
Single Inheritance:
Single inheritance involves a derived class inheriting from a single base class. The derived class 
inherits the properties and methods of the base class.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating.")


class Dog(Animal):
    def bark(self):
        print(self.name + " is barking.")


# Creating an instance of the derived class
my_dog = Dog("Buddy")
my_dog.eat()  # Accessing the method from the base class
my_dog.bark()  # Accessing the method from the derived class

"""
In this example, the class Dog inherits from the class Animal. The Dog class inherits the eat method from the Animal class,
and it also has its own unique method, bark.
"""

"""
Multiple Inheritance:
Multiple inheritance involves a derived class inheriting from multiple base classes. The derived class inherits the
properties and methods of all the base classes.
"""


class Parent1:
    def method1(self):
        print("Parent 1 - Method 1")


class Parent2:
    def method2(self):
        print("Parent 2 - Method 2")


class Child(Parent1, Parent2):
    def method3(self):
        print("Child - Method 3")


# Creating an instance of the derived class
my_child = Child()
my_child.method1()  # Accessing the method from Parent1
my_child.method2()  # Accessing the method from Parent2
my_child.method3()  # Accessing the method from Child

"""
In this example, the class Child inherits from both Parent1 and Parent2. It can access methods from both base classes,
as well as its own unique method.
"""

"""
Multilevel Inheritance:
Multilevel inheritance involves creating a derived class from another derived class.
This forms a parent-child-grandchild relationship between classes.
"""


class Grandparent:
    def method1(self):
        print("Grandparent - Method 1")


class Parent(Grandparent):
    def method2(self):
        print("Parent - Method 2")


class Child(Parent):
    def method3(self):
        print("Child - Method 3")


# Creating an instance of the derived class
my_child = Child()
my_child.method1()  # Accessing the method from Grandparent
my_child.method2()  # Accessing the method from Parent
my_child.method3()  # Accessing the method from Child

"""
In this example, the class Child inherits from the class Parent, which in turn inherits from the class Grandparent.
The Child class can access methods from both its immediate parent and its grandparent.
"""


"""
Hierarchical Inheritance:
Hierarchical inheritance involves multiple derived classes inheriting from a single base class.
Each derived class will have its own unique functionality.
"""


class Vehicle:
    def drive(self):
        print("Vehicle is being driven.")


class Car(Vehicle):
    def accelerate(self):
        print("Car is accelerating.")


class Bike(Vehicle):
    def pedal(self):
        print("Bike is being pedaled.")


# Creating instances of the derived classes
my_car = Car()
my_bike = Bike()

my_car.drive()  # Accessing the method from Vehicle through Car
my_car.accelerate()  # Accessing the method from Car
my_bike.drive()  # Accessing the method from Vehicle through Bike
my_bike.pedal()  # Accessing the method from Bike

"""
In this example, both the Car and Bike classes inherit from the Vehicle class.
Each derived class has its own unique methods but can also access the common functionality defined in the base class.
"""


"""
Method Resolution Order (MRO) is the order in which Python searches for methods and attributes in a class hierarchy during inheritance.
It determines which method or attribute will be called when invoked on an object. 

To understand the MRO, let's consider an example with multiple inheritance: 
"""

class A:
    def method(self):
        print("A's method")

class B(A):
    def method(self):
        print("B's method")

class C(A):
    def method(self):
        print("C's method")

class D(B, C):
    pass

d = D()
d.method()
