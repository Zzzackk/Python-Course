# Concept: How to utilize the imported module "glob", which is to get a list of filepaths that satisfy file pattern
# and then you can access the content of each file using a for loop and inside the for loop you apply the open function
# to each filepath contained in that list.

import glob


myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())

print(myfiles)