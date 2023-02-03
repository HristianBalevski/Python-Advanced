import os

data = input()

while data != 'End':
    data = data.split('-')
    command = data[0]
    file_name = data[1]

    if command == 'Create':
        open(file_name, 'w').close()

    elif command == 'Add':
        content = data[2]

        with open(file_name, 'a') as file:
            file.write(content + '\n')

    elif command == 'Replace':
        old_string = data[2]
        new_string = data[3]

        if os.path.exists(file_name):
            with open(file_name, 'r+') as file:
                text = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(text)
        else:
            print("An error occurred")

    elif command == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
    data = input()
