# Description: Examples of for loops in Python
# for loops in Python are inclusive of the start index and exclusive of the end index.

# basic for loop
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# for loop with start and end
for i in range(2, 5):
    print(i)
# Output: 2 3 4

# for loop with start, end and step
for i in range(2, 10, 2):
    print(i)
# Output: 2 4 6 8

# for loop with negative step (reverse direction)
for i in range(10, 4, -1):
    print(i)
# Output: 10 9 8 7 6 5

# for loop going backwards in steps of 2
for i in range(10, 2, -2):
    print(i)
# Output: 10 8 6 4

# for loop over a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# Output: apple banana cherry

# Three ways to iterate in reverse in Python

# 1. Using the reversed() function:
# This is the most straightforward and readable way to iterate in reverse:
my_list = [1, 2, 3, 4, 5]
for item in reversed(my_list):
    print(item)

# 2. Using the range() function with a negative step:
# This method is useful if you need more control over the iteration, such as stepping by more than one element:
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])

# 3. Using slicing with a negative step:
# This is a concise way to reverse a sequence, but it creates a new reversed copy:
for item in my_list[::-1]:
    print(item)
