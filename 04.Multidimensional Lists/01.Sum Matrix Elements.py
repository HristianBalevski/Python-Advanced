rows, columns = [int(num) for num in input().split(', ')]

matrix = []
total_sum = 0

for row in range(rows):
    numbers = [int(num) for num in input().split(', ')]
    total_sum += sum(numbers)
    matrix.append(numbers)

print(total_sum)
print(matrix)
