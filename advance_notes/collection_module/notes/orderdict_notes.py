# 6. orderdict()

# Example 1. Insertion Order
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])



# Example 2. Equality Comparison
from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('a', 1), ('c', 3), ('b', 2)])

print(od1 == od2)  # Output: False



# Example 3. Reordering Elements
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od.move_to_end('a')  # Moves 'a' to the end
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

od.move_to_end('b', last=False)  # Moves 'b' to the beginning
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])



# Example 4. Removal of Elements
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od.pop('b')  # Removes the key 'b' and returns its value
print(od)  # Output: OrderedDict([('a', 1), ('c', 3)])

od.popitem(last=False)  # Removes and returns the first item
print(od)  # Output: OrderedDict([('c', 3)])



# Example 5. Ordering Operations
from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('b', 2), ('c', 3), ('a', 1)])

print(od1.keys() == od2.keys())  # Output: True



# Example 6. Conversion to Regular Dictionary
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

regular_dict = dict(od)
print(regular_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}



# Example 7. popitem() Method
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

key, value = od.popitem()  # Removes and returns the last item
print(key, value)  # Output: 'c', 3



# Example 8. clear() Method
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od.clear()  # Removes all items from the OrderedDict
print(od)  # Output: OrderedDict()



# Example 9. update() Method
from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('c', 3), ('d', 4)])

od1.update(od2)  # Updates od1 with the key-value pairs from od2
print(od1)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])



# Example 10. copy() Method:
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2)])

od_copy = od.copy()  # Creates a shallow copy of the OrderedDict
print(od_copy)  # Output: OrderedDict([('a', 1), ('b', 2)])
