filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for item in filenames:
    file = open(item, 'w')
    file.write("Hello")
    file.close()
