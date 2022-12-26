rows, cols = [int(num) for num in input().split()]

matrix = []
equal_cells = 0

for _ in range(rows):
    matrix.append(input().split())

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            equal_cells += 1
print(equal_cells)