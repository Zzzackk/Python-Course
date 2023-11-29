# My attempt at making the password checker on my own ^^

password = input("Enter new password: ")

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong Password")
else:
    print("Weak Password")
