rows = int(input())
matrix = []

for row in range(rows):
    numbers = input().split(', ')
    matrix.append([int(num) for num in numbers])
    
even_matrix = [[digit for digit in element if digit % 2 == 0] for element in matrix]
print(even_matrix)