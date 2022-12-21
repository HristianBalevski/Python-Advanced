from sys import maxsize
rows, columns = [int(num) for num in input().split(', ')]

matrix = []

for i in range(rows):
    numbers = [int(num) for num in input().split(', ')]
    matrix.append(numbers)

max_sum = -maxsize
coordinates = []

for row in range(rows - 1):
    for col in range(columns - 1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1],  matrix[row + 1][col], matrix[row + 1][col + 1]]

        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            coordinates = sub_matrix.copy()

print(coordinates[0], coordinates[1])
print(coordinates[2], coordinates[3])
print(max_sum)