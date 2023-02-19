row_size, col_size = [int(num) for num in input().split()]
my_row, my_col = 0, 0
matrix = []

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

players_counter = 0
turns_counter = 0

for row in range(row_size):
    elements = input().split()
    for col in range(col_size):
        if elements[col] == 'B':
            my_row = row
            my_col = col
    matrix.append(elements)

while players_counter < 3:
    command = input()

    if command == 'Finish':
        break

    next_row, next_col = moves[command](my_row, my_col)

    if 0 <= next_row < row_size and 0 <= next_col < col_size:
        if matrix[next_row][next_col] == 'O':
            continue

        elif matrix[next_row][next_col] == 'P':
            players_counter += 1
            turns_counter += 1
            matrix[next_row][next_col] = '-'
        else:
            turns_counter += 1

        my_row, my_col = next_row, next_col

print("Game over!")
print(f"Touched opponents: {players_counter} Moves made: {turns_counter}")
