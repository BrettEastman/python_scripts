#! python3

import re
import pyperclip

# Create a regex object for phone numbers
phoneRegex = re.compile('''(

(\d{3}|\(\d{3}\))?                # area code - optional
(\s|-|\.)?                        # first seperator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # seperator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension number-part - optional
)''', re.VERBOSE)

# Create a regex object for emails
emailRegex = re.compile('''(
[a-zA-Z0-9._+]+    # name part - this is a character class that will search for all these possibilities
@                  # @ symbol
[a-zA-Z0-9._+]+    # domain name part
(\.[a-zA-Z]{2,4})  # dot something 
)''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# Extract email/phone numbers from this list
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

allEmails = []
for eMail in extractedEmail:
    allEmails.append(eMail[0])

# Copy the extracted email/phone numbers to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmails)
pyperclip.copy(results)