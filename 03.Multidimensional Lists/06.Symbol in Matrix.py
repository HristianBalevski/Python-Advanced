size_of_matrix = int(input())
matrix = []

for info in range(size_of_matrix):
    symbols = input()
    matrix.append(symbols)

searched_symbol = input()
symbol_is_find = False

for row in range(size_of_matrix):
    for col in range(size_of_matrix):
        if matrix[row][col] == searched_symbol:
            symbol_is_find = True
            print(f"({row}, {col})")
            break
    if symbol_is_find:
        break

if not symbol_is_find:
    print(f'{searched_symbol} does not occur in the matrix')