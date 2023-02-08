size = int(input())
matrix = []

snake_row = 0
snake_col = 0

first_b_row = 0
first_b_col = 0

second_b_row = 0
second_b_col = 0

f_b_found = False

for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == 'S':
            snake_row = row
            snake_col = col

        elif row_elements[col] == 'B':
            if not f_b_found:
                first_b_row = row
                first_b_col = col
                f_b_found = True
            else:
                second_b_row = row
                second_b_col = col
    matrix.append(row_elements)
matrix[snake_row][snake_col] = '.'

movement = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

food_counter = 0

while True:
    if food_counter >= 10:
        matrix[snake_row][snake_col] = 'S'
        break

    command = input()

    next_row, next_col = movement[command](snake_row, snake_col)

    if 0 <= next_row < size and 0 <= next_col < size:
        if matrix[next_row][next_col] == 'B':
            matrix[next_row][next_col] = '.'
            if next_row == first_b_row and next_col == first_b_col:
                next_row, next_col = second_b_row, second_b_col
            else:
                next_row, next_col = first_b_row, first_b_col
            matrix[next_row][next_col] = '.'

        elif matrix[next_row][next_col] == '*':
            food_counter += 1
            matrix[next_row][next_col] = '.'
        matrix[next_row][next_col] = '.'
        snake_row, snake_col = next_row, next_col
    else:
        print("Game over!")
        break
if food_counter >= 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_counter}")

for row in matrix:
    print(''.join(row))
