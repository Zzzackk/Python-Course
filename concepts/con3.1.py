# Concept: When using a for-loop, like on the example below, the variable 'meal' is created on the fly.
# Concept2: While loop runs as long as the condition is true, and for loop runs as longs as there are items on the list.
# Concept3: You can iterate not only list but other things such as strings, they are treated as sequences of objects.

meals = ['pasta','pizza','salad']

for meal in meals:
    print(meal.capitalize())

print("Bye!")

for char in 'meals':
    print(char.capitalize())