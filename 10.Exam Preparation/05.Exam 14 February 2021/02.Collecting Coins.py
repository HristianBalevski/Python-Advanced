size = int(input())
matrix = []
my_path = []
total_coins = 0
player_wins = False
my_row, my_col = 0, 0

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

for row in range(size):
    elements = input().split()
    for col in range(size):
        if elements[col] == 'P':
            my_row, my_col = row, col
    matrix.append(elements)

my_path.append([my_row, my_col])
while True:
    command = input()
    if command not in moves:
        continue

    next_row, next_col = moves[command](my_row, my_col)
    next_row, next_col = next_row % size, next_col % size

    if matrix[next_row][next_col] == 'X':
        total_coins //= 2
        my_path.append([next_row, next_col])
        break

    if [next_row, next_col] not in my_path:
        total_coins += int(matrix[next_row][next_col])
    my_path.append([next_row, next_col])

    if total_coins >= 100:
        player_wins = True
        break

    my_row, my_col = next_row, next_col

if player_wins:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")
print('Your path:')
for path in my_path:
    print(path)
