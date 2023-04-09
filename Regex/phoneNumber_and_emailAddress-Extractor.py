import pyperclip
import re

# get the text off the clipboard
text = str(pyperclip.paste())
# find all the phone numbers and email addresses in the text
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# Find all the matches
match_phonenum = []
match_email = []

for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != '': # rethink this line 
        phoneNum += ' x' + groups[8] # and this line some thing is wrong with the '8' number
    match_phonenum.append(phoneNum)

for groups in emailRegex.findall(text):
    match_email.append(groups[0])
    
# paste them into the clipboard
if len(match_phonenum) > 0:
    pyperclip.copy('\n'.join(match_phonenum))
    print('Copied to clipboard: ')
    print('\n'.join(match_phonenum))
else:
    print("No phone numbers found.")
if len(match_email) > 0:
    pyperclip.copy('\n'.join(match_email))
    print("Copied to clipboard: ")
    print("\n".join(match_email))
else:
    print("No emails found.")