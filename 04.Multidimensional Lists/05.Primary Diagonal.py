size_of_matrix = int(input())
matrix = []

for info in range(size_of_matrix):
    numbers = [int(num) for num in input().split()]
    matrix.append(numbers)

primary_diagonal = 0
for row in range(size_of_matrix):
    for col in range(size_of_matrix):
        if row == col:
            primary_diagonal += matrix[row][col]
print(primary_diagonal)