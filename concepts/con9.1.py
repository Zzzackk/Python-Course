# Concept1: Using isdigit() and isupper() with for loops to check each item in the string.
# Concept2: Using Dictionaries instead of list because we have multiple values assigned to different variables.
# Concept3: Before checking if something is True its best to assign a False value to it.
# Concept4: Using the all() function that returns True or False based on what all the items in one list or dict are.

password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

if all(result.values()):
    print("Strong Password.")
else:
    print("Weak Password.")
