# Concept1: Using sort method to return a list in order.
# Concept2: You can use waiting_list.sort(reverse=True) to return the items in the reverse order.

waiting_list = ["sen","ben","john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)