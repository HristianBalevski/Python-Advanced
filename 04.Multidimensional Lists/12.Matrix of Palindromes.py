rows, cols = [int(num) for num in input().split()]

for row in range(rows):
    for col in range(cols):
        current_word = chr(row + 97) + chr(row + col + 97) + chr(row + 97)

        if current_word == current_word[::-1]:
            if col + 1 != cols:
                print(current_word, end=' ')
            else:
                print(current_word, end='\n')