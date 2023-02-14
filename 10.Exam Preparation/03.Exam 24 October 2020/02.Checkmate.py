size = 8
chessboard = []
king_row = 0
king_col = 0

king_is_captured = False

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'K':
            king_row = row
            king_col = col
    chessboard.append(row_elements)

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

for direction in mapper:
    next_row, next_col = mapper[direction](king_row, king_col)

    while 0 <= next_row < size and 0 <= next_col < size:
        if chessboard[next_row][next_col] == 'Q':
            king_is_captured = True
            print(f'{[next_row, next_col]}')
            break
        next_row, next_col = mapper[direction](next_row, next_col)
        
if not king_is_captured:
    print('The king is safe!')
