# pop is used to remove an item from a list
# if you do list.pop(0), then it works like shift in javascript
# it could also work like splice in javascript, but you just need the index of the item you want to remove

# The pop() method removes and returns the last element if no index is specified. The remove() method removes the first matching element from the list.

sample_list = [1, 2, 3, 4, 5]
first = sample_list.pop(0)
print(sample_list)         # [2, 3, 4, 5]
print(first)               # 1

sample_list2 = [1, 2, 3, 4, 5]
third = sample_list2.pop(2)
print(sample_list2)         # [1, 2, 4, 5]
print(third)               # 3
