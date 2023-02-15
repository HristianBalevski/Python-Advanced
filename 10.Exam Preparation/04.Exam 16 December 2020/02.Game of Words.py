initial_text = input()
size = int(input())

matrix = []
player_row = 0
player_col = 0

for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
    matrix.append(row_elements)

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

matrix[player_row][player_col] = '-'
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input()
    next_row, next_col = moves[command](player_row, player_col)

    if 0 > next_row or next_row >= size or 0 > next_col or next_col >= size:
        last_char = initial_text[-1]
        if last_char != '':
            initial_text = initial_text[:-1]
            continue
    else:
        if matrix[next_row][next_col] != '-':
            initial_text += matrix[next_row][next_col]
            matrix[next_row][next_col] = '-'
    player_row = next_row
    player_col = next_col

matrix[player_row][player_col] = 'P'

print(initial_text)
for row in matrix:
    print(''.join(row))
