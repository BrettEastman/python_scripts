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
