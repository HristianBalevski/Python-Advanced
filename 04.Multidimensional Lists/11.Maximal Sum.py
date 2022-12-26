from sys import maxsize
rows, cols = [int(num) for num in input().split()]

matrix = []
max_sum = -maxsize
biggest_square = []

for _ in range(rows):
    matrix.append([int(num) for num in input().split()])

for row in range(rows - 2):
    for col in range(cols - 2):
        square = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2], matrix[row + 1][col], matrix[row + 1]
        [col + 1], matrix[row + 1][col + 2], matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]

        if sum(square) > max_sum:
            max_sum = sum(square)
            biggest_square = square

print(f"Sum = {max_sum}")
counter = 1
for number in biggest_square:
    if counter % 3 == 0:
        print(number, end='\n')
    else:
        print(number, end=' ')
    counter += 1