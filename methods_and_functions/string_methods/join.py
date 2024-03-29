# .join() method can join together the elements of an array into a string with the joiner of your choice. For example, if you want to join everything together into one string like a word, you can join with “” as the argument.

# note that the joiner comes FIRST, before the method, then the array comes after - this is the opposite of javascript

# Basic example
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)  # John#Peter#Vicky

# function to join an array of strings into a single string with a joiner


def applyJoin(arrayOfStrings, joiner):
    # create a joinedString variable
    # assign it to a string which is all of the strings in the input array separated by the input string
    joinedString = joiner.join(arrayOfStrings)
    # return the joinedString variable
    return joinedString


resultString1 = applyJoin(['first', 'second', 'third'], '--')
print('should log joined string:', resultString1)
# --> first--second--third

resultString2 = applyJoin(['git', 'commit'], ' ')
print('should also log joined string:', resultString2)
# --> git commit
