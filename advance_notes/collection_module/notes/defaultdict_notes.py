
# 4. defaultdict()

# 1. Creating a defaultdict:
# You can create a defaultdict by passing a callable object or data type as the default factory.
from collections import defaultdict

# Using a callable object as the default factory
d = defaultdict(list)
print(d[1])  # Output: []

# Using a data type as the default factory
d = defaultdict(int)
print(d[1])  # Output: 0

# 2. Default value for missing keys:
# When accessing a key that does not exist in the defaultdict, it returns the default value instead of raising a KeyError.
from collections import defaultdict

d = defaultdict(int)
print(d[1])  # Output: 0
print(d[2])  # Output: 0

# 3. Adding items to a defaultdict:
# You can add items to a defaultdict just like a regular dictionary.
from collections import defaultdict

d = defaultdict(int)
d['apple'] = 5
d['banana'] = 2

print(d)  # Output: defaultdict(<class 'int'>, {'apple': 5, 'banana': 2})

# 4. Accessing items in a defaultdict:
# You can access items in a defaultdict using square bracket notation, just like a regular dictionary.
from collections import defaultdict

d = defaultdict(int)
d['apple'] = 5
d['banana'] = 2

print(d['apple'])   # Output: 5
print(d['orange'])  # Output: 0 (default value for missing key)

# 5. Default factory:
# You can access the default factory object of a defaultdict using the default_factory attribute.
from collections import defaultdict

d = defaultdict(list)
print(d.default_factory)  # Output: <class 'list'>

# 6. Iterating over a defaultdict:
# You can iterate over a defaultdict just like a regular dictionary using loops or iterator methods.
from collections import defaultdict

d = defaultdict(int)
d['apple'] = 5
d['banana'] = 2

for key, value in d.items():
    print(key, value)
# Output:
# apple 5
# banana 2

# 7. Using custom default factories:
# You can use custom functions or lambda expressions as default factories to provide dynamic default values.

# code with normal function
from collections import defaultdict

def default_value():
    return 'N/A'

d = defaultdict(default_value)
print(d[1])  # Output: 'N/A'

# code with lambda function
from collections import defaultdict

d = defaultdict(lambda: 'N/A')
print(d[1])  # Output: 'N/A'


