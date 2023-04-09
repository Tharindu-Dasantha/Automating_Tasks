import re

# Creating a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Matching numbers
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group()) # Return a string of the actual matched text

# Grouping with Parantheses
print("Form here we print the grouped numbers")

mo.group(1) # 415
mo.group(2) # 555-4242
mo.group(0) # 415-555-4242
mo.group() # 415-555-4242

# also can use groups
mo.groups() # ('415', '555-4242')
areaCode, mainNumber = mo.groups() 
print(areaCode) # 415
print(mainNumber) # 555-4242