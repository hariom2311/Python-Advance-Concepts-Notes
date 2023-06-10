# 4. namedtuple()
# Example 1. Accessing elements using dot notation:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 5)

print(p.x)  # Output: 2
print(p.y)  # Output: 5

# Example 2. Indexing and slicing:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 5)

print(p[0])  # Output: 2
print(p[1])  # Output: 5
print(p[:])  # Output: (2, 5)

# Example 3. Iteration:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 5)

for value in p:
    print(value)  # Output: 2\n5

# Example 4. Immutability:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 5)

p.x = 10  # Raises an AttributeError: can't set attribute

# Example 5. Type and Class Names:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

print(type(Point))        # Output: <class 'type'>
print(Point.__name__)     # Output: 'Point'

# Example 6. Tuple Operations:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(2, 5)
p2 = Point(4, 9)

p3 = p1 + p2
print(p3)      # Output: Point(x=6, y=14)

print(p1 * 2)  # Output: Point(x=2, y=5, x=2, y=5)

# Example 7. _fields Attribute:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

print(Point._fields)  # Output: ('x', 'y')


# Example 8. _make() Method:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
values = (3, 7)

p = Point._make(values)
print(p)  # Output: Point(x=3, y=7)

# Example 9. _asdict() Method:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 5)

print(p._asdict())  # Output: {'x': 2, 'y': 5}

# Example 10. _replace() Method:
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 5)

p2 = p._replace(x=10)
print(p2)  # Output: Point(x=10, y=5)


