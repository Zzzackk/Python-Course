# Concept1: Using the zip function to create files with specific names and contents assigned to each of them.
# Concept2: Using "../" to move up a directory in the project files.
# Concept3: Decreasing lines in a list  by just pressing enter after coma.
# Concept4: Decreasing lines in single string by pressing enter, then the string will be encapsulated by ()

example = ("I love eating"
           " carrots")

contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)

print(example)
print(type(example))