# String Formatting
# contatenating using the Conversion Specifier - %s

name = 'Suzy'
place = 'Scopa'
time = 'sundown'
food = 'caviar'

sentence = 'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (
    name, place, time, food)

# Hello Suzy, you are invited to a party at Scopa at sundown. Please bring caviar.
print(sentence)
