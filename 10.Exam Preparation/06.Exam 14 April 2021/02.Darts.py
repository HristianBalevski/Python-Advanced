from collections import deque

SIZE = 7

players = deque(input().split(', '))
darts = [input().split() for _ in range(SIZE)]

info_dict = {}
total_points = 0

for player in players:
    info_dict[player] = [501, 0]

mapper = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

while True:
    row, col = eval(input())
    current_player = players[0]
    info_dict[current_player][1] += 1

    if 0 <= row < SIZE and 0 <= col < SIZE:

        if darts[row][col] == 'B':
            print(f"{current_player} won the game with {info_dict[current_player][1]} throws!")
            break

        elif darts[row][col] == 'D':

            for direction in mapper:
                next_row, next_col = mapper[direction](row, col)

                while 0 <= next_row < SIZE and 0 <= next_col < SIZE:
                    current_pos = darts[next_row][next_col]
                    if current_pos != 'D' and current_pos != 'B' and current_pos != 'T':
                        total_points += int(darts[next_row][next_col]) * 2

                    next_row, next_col = mapper[direction](next_row, next_col)

        elif darts[row][col] == 'T':

            for direction in mapper:
                next_row, next_col = mapper[direction](row, col)

                while 0 <= next_row < SIZE and 0 <= next_col < SIZE:
                    current_pos = darts[next_row][next_col]
                    if current_pos != 'D' and current_pos != 'B' and current_pos != 'T':
                        total_points += int(darts[next_row][next_col]) * 3

                    next_row, next_col = mapper[direction](next_row, next_col)
        else:
            total_points += int(darts[row][col])

        info_dict[current_player][0] -= total_points
        total_points = 0

        if info_dict[current_player][0] <= 0:
            print(f"{current_player} won the game with {info_dict[current_player][1]} throws!")
            break

    players.rotate()
