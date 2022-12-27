size = int(input())

matrix = []

for _ in range(size):
    elements = [int(num) for num in input().split()]
    matrix.append(elements)

while True:
    data = input().split()
    command = data[0]
    
    if command == 'END':
        break
    
    row, col, value = [int(num) for num in data[1:]]

    if 0 <= row < size and 0 <= col < size:
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)
