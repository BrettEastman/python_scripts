#! python3

import re
import pyperclip

# Create a regex object for phone numbers
phoneRegex = re.compile('''

((\d\d\d)|(\(\d\d\d)))?   # area code - optional
(\s|-)                    # first seperator
\d\d\d                    # first 3 digits
-                         # seperator
\d\d\d\d                  # last 4 digits
(((ext(\.)?\s)|x)         # extension word-part - optional
(\d{2,5}))?               # extension number-part - optional
''', re.VERBOSE)

# Create a regex object for emails
emailRegex = re.compile('''
[a-zA-Z0-9._+]+    # name part - this is a character class that will search for all these possibilities
@                  # @ symbol
[a-zA-Z0-9._+]+    # domain name part
''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste

# Extract email/phone numbers from this list
extractedPhone = phoneRegex.findall()
extractedEmail = emailRegex.findall()

print(extractedPhone)
print(extractedEmail)

# Copy the extracted email/phone numbers to the clipboard
