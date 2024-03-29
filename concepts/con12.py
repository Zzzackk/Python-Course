# Concept: Decoupling the output to get clean and concise output from functions instead of a whole string, for example.

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("Enter feet and inches: ")

result = convert(feet_inches)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide.")
