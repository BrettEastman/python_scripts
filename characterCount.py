# This program will count the characters of all strings, including extremely long texts with millions of lines

# this is to import pretty print
import pprint

message = 'It was a bright cold day in April, and the clock struck 13'
count = {}

for character in message.lower():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)