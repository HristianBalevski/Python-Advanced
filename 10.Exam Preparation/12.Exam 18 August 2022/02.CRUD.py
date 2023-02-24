size = 6
matrix = [[x for x in input().split()] for _ in range(size)]
row, col = eval(input())

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

while True:
    data = input()

    if data == 'Stop':
        break

    data = data.split(', ')
    command = data[0]
    direction = data[1]

    next_row, next_col = moves[direction](row, col)

    if command == 'Create':
        value = data[2]

        if matrix[next_row][next_col] == '.':
            matrix[next_row][next_col] = value

    elif command == 'Update':
        value = data[2]

        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = value

    elif command == 'Delete':
        if matrix[next_row][next_col] != '.':
            matrix[next_row][next_col] = '.'

    elif command == 'Read':
        if matrix[next_row][next_col] != '.':
            print(matrix[next_row][next_col])

    row = next_row
    col = next_col

for r in matrix:
    print(" ".join(r))
