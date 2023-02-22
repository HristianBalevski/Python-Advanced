from collections import deque

size = 6
matrix = []
start_row = 0
start_col = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'E':
            start_row = row
            start_col = col
    matrix.append(row_elements)

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

list_of_commands = deque(input().split(', '))
while True:
    if len(list_of_commands) == 0:
        break

    command = list_of_commands.popleft()
    next_row, next_col = moves[command](start_row, start_col)

    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        next_row = next_row % size
        next_col = next_col % size

    if matrix[next_row][next_col] == 'R':
        print(f"Rover got broken at {next_row, next_col}")
        break

    elif matrix[next_row][next_col] == 'W':
        water_deposit += 1
        print(f'Water deposit found at {next_row, next_col}')

    elif matrix[next_row][next_col] == 'M':
        metal_deposit += 1
        print(f'Metal deposit found at {next_row, next_col}')

    elif matrix[next_row][next_col] == 'C':
        concrete_deposit += 1
        print(f'Concrete deposit found at {next_row, next_col}')

    start_row = next_row
    start_col = next_col


if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
