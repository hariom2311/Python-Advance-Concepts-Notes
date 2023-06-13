
# 3. Deque()

# Example 1. General Explanation of Deque
from collections import deque

d = deque()

# Adding elements to the deque
d.append(1)
d.append(2)
d.append(3)

print(d)  # Output: deque([1, 2, 3])

# Removing elements from the deque
d.pop()
d.popleft()

print(d)  # Output: deque([2])

# Methods used in Deque

# 1. append(x): This method adds element x to the right side of the deque.
from collections import deque

d = deque([1, 2, 3])
d.append(4)
print(d)  # Output: deque([1, 2, 3, 4])


# 2. appendleft(x): This method adds element x to the left side of the deque.
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3])

# 3. clear(): This method removes all elements from the deque, leaving it empty.
from collections import deque

d = deque([1, 2, 3])
d.clear()
print(d)  # Output: deque([])

# 4. copy(): This method creates a shallow copy of the deque.
from collections import deque

d = deque([1, 2, 3])
d_copy = d.copy()
print(d_copy)  # Output: deque([1, 2, 3])

# 5. count(x): This method counts the number of deque elements equal to x.
from collections import deque

d = deque([1, 2, 2, 3])
count = d.count(2)
print(count)  # Output: 2

# 6. extend(iterable): This method extends the right side of the deque by appending elements from the iterable argument.
from collections import deque

d = deque([1, 2, 3])
d.extend([4, 5])
print(d)  # Output: deque([1, 2, 3, 4, 5])

# 7. extendleft(iterable): This method extends the left side of the deque by appending elements from the iterable argument.
# Note that the order of elements in the iterable argument is reversed in the deque.
from collections import deque

d = deque([3, 4, 5])
d.extendleft([1, 2])
print(d)  # Output: deque([2, 1, 3, 4, 5])

# 8. index(x[, start[, stop]]): This method returns the position of x in the deque, starting from start index (default is the beginning)
# and searching up to stop index (default is the end). It raises a ValueError if x is not found.
from collections import deque

d = deque([1, 2, 3, 2, 4])
index = d.index(2) 
index_1 = d.index(2, 2, 4)
print(index)  # Output: 1

# 9. insert(i, x): This method inserts element x into the deque at position i.
from collections import deque

d = deque([1, 2, 3])
d.insert(1, 4)
print(d)  # Output: deque([1, 4, 2, 3])

# 10. remove(value): This method removes the first occurrence of value from the deque. If the value is not found, it raises a ValueError.
from collections import deque

d = deque([1, 2, 3, 2, 4])
d.remove(2)
print(d)  # Output: deque([1, 3, 2, 4])

# 11. reverse(): This method reverses the elements of the deque in-place and returns None.
from collections import deque

d = deque([1, 2, 3])
d.reverse()
print(d)  # Output: deque([3, 2, 1])

# 12. rotate(n=1): This method rotates the deque n steps to the right. If n is negative, it rotates to the left.
from collections import deque

d = deque([1, 2, 3, 4, 5])
d.rotate(2)
print(d)  # Output: deque([4, 5, 1, 2, 3])

d.rotate(-1)
print(d)  # Output: deque([5, 1, 2, 3, 4])
