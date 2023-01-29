number_of_presents = int(input())
size = int(input())

matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0
all_nice_kids = 0

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row = row
            santa_col = col

        elif row_elements[col] == 'V':
            nice_kids += 1
            all_nice_kids += 1
    matrix.append(row_elements)
matrix[santa_row][santa_col] = '-'

while True:
    command = input()

    if command == "Christmas morning" or number_of_presents == 0:
        matrix[santa_row][santa_col] = 'S'
        break

    next_row, next_col = moves[command](santa_row, santa_col)

    if 0 <= next_row < size and 0 <= next_col < size:
        if matrix[next_row][next_col] == 'V':
            number_of_presents -= 1
            nice_kids -= 1
            santa_row = next_row
            santa_col = next_col
            matrix[santa_row][santa_col] = '-'
            if number_of_presents == 0:
                matrix[santa_row][santa_col] = 'S'
                break

        elif matrix[next_row][next_col] == 'C':
            matrix[next_row][next_col] = 'S'
            santa_row = next_row
            santa_col = next_col

            for direction in moves:
                next_row, next_col = moves[direction](santa_row, santa_col)

                if matrix[next_row][next_col] == 'V':
                    number_of_presents -= 1
                    nice_kids -= 1
                    matrix[next_row][next_col] = '-'
                    if number_of_presents == 0:
                        break

                elif matrix[next_row][next_col] == 'X':
                    number_of_presents -= 1
                    matrix[next_row][next_col] = '-'
                    if number_of_presents == 0:
                        break
            break

        matrix[next_row][next_col] = '-'
        santa_row = next_row
        santa_col = next_col

if number_of_presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")
[print(*row) for row in matrix]

if nice_kids == 0:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
