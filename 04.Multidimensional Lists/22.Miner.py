size = int(input())
data = input().split()
matrix = []
miner_row = 0
miner_col = 0
coal_counter = 0
collected_coal = 0
final_row = 0
final_col = 0
game_finish = False

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
coal_position = {}

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 's':
            miner_row = row
            miner_col = col
        elif row_elements[col] == 'c':
            coal_counter += 1
            coal_position[row] = [row, col]
    matrix.append(row_elements)
commands_counter = 0
while True:
    if collected_coal == coal_counter:
        print(f"You collected all coal! ({final_row}, {final_col})")
        break
    elif commands_counter == len(data):
        break
    for command in data:
        commands_counter += 1

        next_row, next_col = moves[command](miner_row, miner_col)
        if 0 <= next_row < size and 0 <= next_col < size:

            if matrix[next_row][next_col] == 'e':
                print(f"Game over! ({next_row}, {next_col})")
                game_finish = True
                final_row = next_row
                final_col = next_col
                break

            elif matrix[next_row][next_col] == 'c':
                collected_coal += 1
                matrix[next_row][next_col] = '*'
                if collected_coal == coal_counter:
                    game_finish = True
                    final_row = next_row
                    final_col = next_col
                    print(f'You collected all coal! ({next_row}, {next_col})')
                    break
        else:
            continue
        miner_row = next_row
        miner_col = next_col
        final_row = next_row
        final_col = next_col
    if game_finish:
        break
if collected_coal < coal_counter and not game_finish:
    print(f'{coal_counter - collected_coal} pieces of coal left. ({final_row}, {final_col})')
