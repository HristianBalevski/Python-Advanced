rows, cols = [int(num) for num in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([num for num in input().split()])

data = input()

while data != 'END':
    data = data.split()

    if data[0] != 'swap' or len(data) != 5:
        print('Invalid input!')
        data = input()
        continue
    else:
        command = data[0]

        num_1, num_2, num_3, num_4 = [int(num) for num in data[1:]]
        if num_1 < 0 or num_2 < 0 or num_3 < 0 or num_4 < 0 or num_1 >= rows or num_2 >= cols or num_3 >= rows or num_4 >= cols:
            print('Invalid input!')
            data = input()
            continue

        matrix[num_1][num_2], matrix[num_3][num_4] = matrix[num_3][num_4], matrix[num_1][num_2]
        for row in matrix:
            print(*row, sep=' ')

    data = input()