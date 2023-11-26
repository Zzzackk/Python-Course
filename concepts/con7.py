# Concept: Using List Comprehensions for replacing and adding elements to items(str) inside an existing list.

filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)