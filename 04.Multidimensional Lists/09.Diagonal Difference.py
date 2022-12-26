size = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(size):
    matrix.append([int(num) for num in input().split()])

for row in range(size):
    for col in range(size):
        if row == col:
            primary_diagonal.append(matrix[row][col])

        if row + col == size - 1:
            secondary_diagonal.append(matrix[row][col])
result = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(result)