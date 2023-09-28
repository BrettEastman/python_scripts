# replace method
print('Enter a word')
oldword = input()
text = oldword + ' is the current word.'
print('text: ' + text)

print('Enter a new word.')
newword = input()

replaced = text.replace(oldword, newword)

print('replaced: ' + replaced)

###

spam = 'Hello there!'
print('original spam: ' + spam)

# spam.replace('e', '*****')
print('replaced spam: ' + spam.replace('e', '*****'))