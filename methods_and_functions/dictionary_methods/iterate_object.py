# how to iterate over an object:

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterate over keys
for key in my_dict:
    print(key)

# Iterate over keys and values
for key, value in my_dict.items():
    print(key, value)

# Iterate over keys and values (Python 3)
for key, value in my_dict.items():
    print(key, '->', value)
