size = int(input())
matrix = []
submarine_row = 0
submarine_col = 0

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == 'S':
            submarine_row = row
            submarine_col = col
    matrix.append(row_elements)
matrix[submarine_row][submarine_col] = '-'

taken_damage = 0
battle_cruisers = 3
last_coordinates = []

while True:
    command = input()

    next_row, next_col = moves[command](submarine_row, submarine_col)

    if matrix[next_row][next_col] == '*':
        taken_damage += 1
        matrix[next_row][next_col] = '-'

        if taken_damage == 3:
            last_coordinates = next_row, next_col
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{last_coordinates[0]}, {last_coordinates[1]}]!")
            break

    elif matrix[next_row][next_col] == 'C':
        battle_cruisers -= 1
        matrix[next_row][next_col] = '-'

        if battle_cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    submarine_row = next_row
    submarine_col = next_col
    
matrix[next_row][next_col] = 'S'

for row in matrix:
    print(''.join(row))
