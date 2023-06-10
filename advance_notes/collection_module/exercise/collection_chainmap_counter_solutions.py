
"""
Question 1
Combine two dictionaries into a single dictionary using ChainMap and update the values of common keys.
"""
# Solution 1

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = dict(ChainMap(dict1, dict2))
print(combined_dict)

# ====================================================================================

"""
Question 2
Update the values of a key in multiple dictionaries using ChainMap.
"""

# Solution 2
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = ChainMap(dict1, dict2)
combined_dict['b'] = 5
print(dict1)
print(dict2)


# ====================================================================================\

"""
Question 3
Count the frequency of each element in a list using Counter.
"""

# Solution 3

from collections import Counter

elements = [1, 2, 3, 1, 2, 1, 3, 4, 2, 2, 1]

element_counts = Counter(elements)
print(element_counts)

# ====================================================================================

"""
Question 4
Find the most common elements and their frequencies in a list using Counter.
"""
# Solution 4
from collections import Counter

elements = [1, 2, 3, 1, 2, 1, 3, 4, 2, 2, 1]

most_common_elements = Counter(elements).most_common(2)
print(most_common_elements)
