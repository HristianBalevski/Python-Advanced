size = int(input())
number_of_bombs = int(input())
matrix = [[0] * size for _ in range(size)]

mapper = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up_left': lambda r, c: (r - 1, c - 1),
    'up_right': lambda r, c: (r - 1, c + 1),
    'down_left': lambda r, c: (r + 1, c - 1),
    'down_right': lambda r, c: (r + 1, c + 1)
}

for _ in range(number_of_bombs):
    bomb_row, bomb_col = eval(input())
    matrix[bomb_row][bomb_col] = '*'

for row in range(size):
    for col in range(size):
        for command in mapper:
            if matrix[row][col] == '*':
                next_row, next_col = mapper[command](row, col)
                if 0 <= next_row < size and 0 <= next_col < size and matrix[next_row][next_col] != '*':
                    matrix[next_row][next_col] += 1

for row in matrix:
    print(' '.join([str(el) for el in row]))
