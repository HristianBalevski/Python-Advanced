from Hris import create_sequence, locate_index

while True:
    data = input()
    if data == 'Stop':
        break

    data = data.split()
    command = data[0]

    if command == 'Create':
        number = int(data[2])
        print(create_sequence(number))
    else:
        number = int(data[1])
        print(locate_index(number))
