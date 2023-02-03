from os import walk

stored_data = {}

for _, _, files in walk('.'):
    for file in files:
        extension = file.split('.')[-1]

        if extension not in stored_data:
            stored_data[extension] = []
        stored_data[extension].append(file)

with open('result.txt', 'w') as output:
    for extension, files in sorted(stored_data.items()):
        output.write(f'.{extension}\n')

        for file in sorted(files):
            output.write(f'- - - {file}\n')
