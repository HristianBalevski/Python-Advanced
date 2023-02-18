board = [input().split() for _ in range(6)]
points = 0
needed_points = 0
collected_points = []

mapper = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

for _ in range(3):

    row, col = eval(input())

    if 0 <= row < 6 and 0 <= col < 6 and board[row][col] == 'B':
        for direction in mapper:
            next_row, next_col = mapper[direction](row, col)
            while 0 <= next_row < 6 and 0 <= next_col < 6:
                current_position = board[next_row][next_col]
                if current_position != 'B' and [next_row, next_col] not in collected_points:
                    collected_points.append([next_row, next_col])
                    points += int(current_position)
                next_row, next_col = mapper[direction](next_row, next_col)
prize = ''
if 100 <= points <= 199:
    prize = 'Football'

elif 200 <= points <= 299:
    prize = 'Teddy Bear'

elif points >= 300:
    prize = 'Lego Construction Set'
else:
    needed_points = 100 - points
if prize != '':
    print(f"Good job! You scored {points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {needed_points} points more to win a prize.")
