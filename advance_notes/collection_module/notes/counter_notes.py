
# 2. Counter()

# Example 1. Creating Counter from iterable, mapping and keywords arguments
from collections import Counter

c = Counter('gallahad') # Creating a new counter from an iterable:
print(c)  # Output: Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})

c = Counter({'red': 4, 'blue': 2}) # Creating a new counter from a mapping:
print(c)  # Output: Counter({'red': 4, 'blue': 2})

c = Counter(cats=4, dogs=8) # Creating a new counter using keyword arguments:
print(c)  # Output: Counter({'dogs': 8, 'cats': 4})

# =====================================================================================

# Example 2. Creating Couter from Iterable using for loop
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)  # Output: Counter({'blue': 3, 'red': 2, 'green': 1})

# ======================================================================================

# Example 3. Creating Couter from List, String and Sentence

from collections import Counter

# Count the frequency of elements in a list
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(my_list)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Count the frequency of characters in a string
my_string = 'abracadabra'
counter = Counter(my_string)
print(counter)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Count the frequency of words in a sentence
my_sentence = 'The quick brown fox jumps over the lazy dog'
word_list = my_sentence.split()
counter = Counter(word_list)
print(counter)  # Output: Counter({'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1})

# =======================================================================================

# Example 4. Basic Operations with Counters

from collections import Counter

# Create Counters
counter1 = Counter({'a': 3, 'b': 2, 'c': 1})
counter2 = Counter({'b': 2, 'c': 2, 'd': 1})

# Addition
combined_counter = counter1 + counter2
print(combined_counter)  # Output: Counter({'a': 3, 'b': 4, 'c': 3, 'd': 1})

# Subtraction
subtracted_counter = counter1 - counter2
print(subtracted_counter)  # Output: Counter({'a': 3})

# Intersection
intersected_counter = counter1 & counter2
print(intersected_counter)  # Output: Counter({'b': 2, 'c': 1})

# Union
union_counter = counter1 | counter2
print(union_counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 2, 'd': 1})

# ===================================================================================

# Example 5. Here's an explanation of each method in the Counter class, along with example code:

# 1. total(): Returns the sum of all counts in the Counter.
from collections import Counter

c = Counter({'red': 4, 'blue': 2})
total_count = c.total()
print(total_count)  # Output: 6

# 2. clear(): Resets all counts in the Counter to zero.
from collections import Counter

c = Counter({'red': 4, 'blue': 2})
print(c)  # Output: Counter({'red': 4, 'blue': 2})

c.clear()
print(c)  # Output: Counter()

# 3. list(c): Returns a list of unique elements from the Counter.
from collections import Counter

c = Counter('gallahad')
unique_elements = list(c)
print(unique_elements)  # Output: ['g', 'a', 'l', 'h', 'd']

# 4. set(c): Converts the Counter to a set of unique elements.
from collections import Counter

c = Counter('gallahad')
unique_set = set(c)
print(unique_set)  # Output: {'a', 'd', 'h', 'g', 'l'}

# 5. dict(c): Converts the Counter to a regular dictionary.
from collections import Counter

c = Counter('gallahad')
regular_dict = dict(c)
print(regular_dict)  # Output: {'g': 1, 'a': 3, 'l': 2, 'h': 1, 'd': 1}

# 6. c.items(): Returns a list of (elem, count) pairs in the Counter.
from collections import Counter

c = Counter('gallahad')
items_list = c.items()
print(items_list)  # Output: dict_items([('g', 1), ('a', 3), ('l', 2), ('h', 1), ('d', 1)])

# 7. Counter(dict(list_of_pairs)): Converts a list of (elem, count) pairs to a Counter.
from collections import Counter

list_of_pairs = [('a', 3), ('b', 2), ('c', 1)]
c = Counter(dict(list_of_pairs))
print(c)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})

list_of_pairs = [('a', 3), ('b', 2), ('c', 1)]
c = Counter(list_of_pairs)
print(c)

list_of_pairs = [('a', 3), ('b', 2), ('c', 1)]
c = Counter(list_of_pairs)
print(c)

list_of_pairs = [('a', 3), ('b', 2), ['c', 1]]
c = Counter(list_of_pairs)
print(c)


# 8. c.most_common()[:-n-1:-1]: Returns the n least common elements as a list of (elem, count) pairs.
from collections import Counter

c = Counter({'red': 4, 'blue': 2, 'green': 1, 'yellow': 5})
least_common = c.most_common()[:-2-1:-1]  # Retrieve 2 least common elements
print(least_common)  # Output: [('green', 1), ('blue', 2)]

# 9. +c: Creates a new Counter that includes only positive counts from c.
from collections import Counter

c = Counter({'red': -2, 'blue': 4, 'green': 1})
positive_counts = +c
print(positive_counts)  # Output: Counter({'blue': 4, 'green': 1})
