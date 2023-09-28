# The remove () method is also a common method used to remove and return the list element. Unlike the pop() method, when you make use of the remove() method, you have to specify the particular element to be removed as a method parameter.

# The pop() method removes and returns the last element if no index is specified. The remove() method removes the first matching element from the list.

sample_list = [1, 2, 3, 4, 5]
sample_list.remove(sample_list[0])
print(sample_list)
# [2, 3, 4, 5]
