rows, columns = [int(digit) for digit in input().split(', ')]
matrix = []

for iteration in range(rows):
    elements = [int(num) for num in input().split()]
    matrix.append(elements)

for column_index in range(columns):
    total_sum = 0
    for row_index in range(rows):
        total_sum += matrix[row_index][column_index]
    print(total_sum)