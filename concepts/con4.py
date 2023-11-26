# Concept1: Strings are immutable, one way to go past that is using replace method and over-place the old variable.
# Concept2: Tuples, like strings, are immutable, so, unlike a list, you cant replace the items inside a tuple.

filenames_tuple = ("1.Raw Data.txt","2.Reports.txt","3.Presentations.txt")

filenames = ["1.Raw Data.txt","2.Reports.txt","3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)