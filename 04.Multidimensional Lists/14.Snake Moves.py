rows, cols = [int(num) for num in input().split()]
word = input()

index = 0

for row in range(rows):
    symbols = [None] * cols

    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, - 1, - 1)
    for col in range(start, end, step):
        symbols[col] = word[index % len(word)]
        index += 1
    print(''.join(symbols))