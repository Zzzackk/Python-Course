# Concept: Using with context manager in other scenario and some other new little things.

date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(f"Your mood was: {mood}/10." + 2 * "\n")
    file.write(thoughts)