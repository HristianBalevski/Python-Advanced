size_row, size_col = [int(x) for x in input().split(', ')]
my_row, my_col = 0, 0

workshop = []
all_items_are_collected = False

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

christmas_items = {
    'Christmas decorations': [0, 0],
    'Gifts': [0, 0],
    'Cookies': [0, 0]
}

for row in range(size_row):
    elements = input().split()

    for col in range(size_col):
        if elements[col] == 'Y':
            my_row, my_col = row, col

        elif elements[col] == 'D':
            christmas_items['Christmas decorations'][0] += 1

        elif elements[col] == 'G':
            christmas_items['Gifts'][0] += 1

        elif elements[col] == 'C':
            christmas_items['Cookies'][0] += 1
    workshop.append(elements)
workshop[my_row][my_col] = 'x'

while True:
    data = input().split('-')
    command = data[0]

    if command == 'End':
        break

    step = int(data[1])

    next_row, next_col = moves[command](my_row, my_col)
    next_row = next_row % size_row
    next_col = next_col % size_col

    for i in range(step):
        next_row = next_row % size_row
        next_col = next_col % size_col

        if workshop[next_row][next_col] == 'D':
            christmas_items['Christmas decorations'][0] -= 1
            christmas_items['Christmas decorations'][1] += 1

        elif workshop[next_row][next_col] == 'G':
            christmas_items['Gifts'][0] -= 1
            christmas_items['Gifts'][1] += 1

        elif workshop[next_row][next_col] == 'C':
            christmas_items['Cookies'][0] -= 1
            christmas_items['Cookies'][1] += 1

        workshop[next_row][next_col] = 'x'
        my_row, my_col = next_row, next_col
        next_row, next_col = moves[command](my_row, my_col)

        if christmas_items['Christmas decorations'][0] == 0 and christmas_items['Gifts'][0] == 0 and christmas_items['Cookies'][0] == 0:
            all_items_are_collected = True
            break
    if all_items_are_collected:
        print("Merry Christmas!")
        break

workshop[my_row][my_col] = 'Y'

print("You've collected:")
print(f"- {christmas_items['Christmas decorations'][1]} Christmas decorations")
print(f"- {christmas_items['Gifts'][1]} Gifts")
print(f"- {christmas_items['Cookies'][1]} Cookies")
[print(*row) for row in workshop]
