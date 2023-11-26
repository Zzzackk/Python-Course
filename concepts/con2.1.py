# Concept: While-loop using a condition instead of just 'True'

password = input("Enter the password:")

while password != "pass123":
    password = input("Enter the password:")

print("Password was correct!")