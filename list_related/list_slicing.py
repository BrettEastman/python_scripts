# Python List Slicing Syntax
# The format for list slicing is of Python List Slicing is as follows:

# list[ Initial : End : IndexJump ]

# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]

# Display entire list
print(Lst[::])

# Display entire list using negative indexing
print(Lst[-7::1])

# Display section of list beginning at initial index and going up to but not including the end index
print(Lst[1:5]) # [70, 30, 20, 90]


# Initialize new list
Lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Display sliced list
print(Lst2[3:9:2]) # [4, 6, 8]

# Display sliced list
print(Lst2[::2]) # [1, 3, 5, 7, 9]

# Display reversed list
print(Lst2[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# from index 4 on
print(Lst2[4:]) # [5, 6, 7, 8, 9]

# up to index 4
print(Lst2[:4]) # [1, 2, 3, 4]