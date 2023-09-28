# Split doesn't work the same way in Python as it does in Javascrip

# 1) you can use a standard for loop to iterate over each character in a string and append it to a list
input_string = "Hello, World!"

char_list = []

for char in input_string:
    char_list.append(char)

# 2) Or you can use a list comprehension to do the same thing in one line
char_list = [char for char in input_string]


# Either way, char_list now contains individual characters as elements
print(char_list) # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

