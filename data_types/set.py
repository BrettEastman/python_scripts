# Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
# Once a set is created, you cannot change its items, but you can remove items and add new items. Duplicates are not allowed. Sets cannot have two items with the same value.

fruits = {"apple", "banana", "cherry"}

# A set can contain different data types.
set1 = {"abc", 34, True, 40, "male"}

# The values True and 1 are considered the same value in sets, and are treated as duplicates. The values False and 0 are considered the same value in sets, and are treated as duplicates.
bools_set = {True, True, True}
print(bools_set)  # {True}

myset = {1, False, 0}
print(myset)  # {0, 1}

# You cannot access items in a set by referring to an index or a key. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in myset:
    print(x)

# To add one item to a set use the add() method.
myset.add("orange")
print(myset)  # {0, 1, 'orange'}

# To add more than one item to a set use the update() method.
myset.update(["orange", "mango", "grapes"])
print(myset)  # {0, 1, 'orange', 'mango', 'grapes'}

# To determine how many items a set has, use the len() method.
print(len(myset))  # 5

# To remove an item in a set, use the remove(), or the discard() method.
myset.remove("orange")
print(myset)  # {0, 1, 'mango', 'grapes'}

# If the item to remove does not exist, remove() will raise an error.
# myset.remove("banana")  # KeyError: 'banana'

# If the item to remove does not exist, discard() will NOT raise an error.
myset.discard("banana")
print(myset)  # {0, 1, 'mango', 'grapes'}
