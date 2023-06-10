# 1. ChainMap()

# Example 1: Merging Multiple Dictionaries

from collections import ChainMap

# Define multiple dictionaries
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'occupation': 'Engineer'}
dict3 = {'language': 'Python', 'experience': '5 years'}

# Create a ChainMap by merging the dictionaries
chain_map = ChainMap(dict1, dict2, dict3)

# Accessing keys and values
print(chain_map['name'])  # Output: Alice
print(chain_map['city'])  # Output: New York

# Modifying a key in the ChainMap
chain_map['age'] = 30
print(dict1)  # Output: {'name': 'Alice', 'age': 30}
# =====================================================================


# Example 2: Updating Values

from collections import ChainMap

# Define dictionaries
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'occupation': 'Engineer'}

# Create a ChainMap
chain_map = ChainMap(dict1, dict2)

# Updating values
chain_map.update({'age': 30, 'occupation': 'Software Developer'})
print(chain_map['age'])  # Output: 30
print(chain_map['occupation'])  # Output: Software Developer
# =======================================================================

# Example 3: Reordering the ChainMap

from collections import ChainMap

# Define dictionaries
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'occupation': 'Engineer'}

# Create a ChainMap
chain_map = ChainMap(dict1, dict2)

# Reordering the ChainMap
reordered_chain_map = chain_map.new_child(dict2)
print(reordered_chain_map['name'])  # Output: Alice (from dict1)
print(reordered_chain_map['city'])  # Output: New York (from dict2)

#======================================================================

# Example 4: Accessing Keys and Values Iteratively

from collections import ChainMap

# Define dictionaries
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'occupation': 'Engineer'}

# Create a ChainMap
chain_map = ChainMap(dict1, dict2)

# Iterating over keys and values
for key, value in chain_map.items():
    print(key, value)

