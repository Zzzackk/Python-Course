# Concept: You can't access local variable in the code except when you return it with a custom function.

def greet():
    message = "hello"
    new_message = message.capitalize()
    return new_message


greeting = greet()
print(greeting)

# print(new_message) Impossible to print because technically they don't exist globally.
# print(message)