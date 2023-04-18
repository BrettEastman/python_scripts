def quick_sort(sequence):
  length = len(sequence)
  if length <= 1:
    return sequence
  else:
    pivot = sequence.pop()

  items_greater = []
  items_lesser = []

  for item in sequence:
    if item > pivot:
      items_greater.append(item)

    else:
      items_lesser.append(item)

  return quick_sort[items_lesser] + [pivot] + quick_sort[items_greater]

# unsorted_list = [2,5,3,7,9,556,34,6,0,11]

# print(quick_sort(unsorted_list))

print(quick_sort([2,5,3,7,9,556,34,6,0,11]))
