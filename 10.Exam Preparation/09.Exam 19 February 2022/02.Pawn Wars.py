def white_checker(r, c):
    if r - 1 == black_pawn_position[0][0] and c - 1 == black_pawn_position[0][1]:
        white_pawn_position[0][0] = r - 1
        white_pawn_position[0][1] = c - 1
        return white_pawn_position[0][0], white_pawn_position[0][1]
    elif r - 1 == black_pawn_position[0][0] and c + 1 == black_pawn_position[0][1]:
        white_pawn_position[0][0] = r - 1
        white_pawn_position[0][1] = c + 1
        return white_pawn_position[0][0], white_pawn_position[0][1]
    return False


def black_checker(r, c):
    if r + 1 == white_pawn_position[0][0] and c + 1 == white_pawn_position[0][1]:
        black_pawn_position[0][0] = r + 1
        black_pawn_position[0][1] = c + 1
        return black_pawn_position[0][0], black_pawn_position[0][1]
    elif r + 1 == white_pawn_position[0][0] and c - 1 == white_pawn_position[0][1]:
        black_pawn_position[0][0] = r + 1
        black_pawn_position[0][1] = c - 1
        return black_pawn_position[0][0], black_pawn_position[0][1]
    return False


size = 8
chessboard = []
white_pawn_position = []
black_pawn_position = []

columns = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}

game_over = False

for row in range(size):
    elements = input().split()
    for col in range(size):
        if elements[col] == 'w':
            white_pawn_position.append([row, col])
        elif elements[col] == 'b':
            black_pawn_position.append([row, col])
    chessboard.append(elements)

current_pawn, second_pawn = 'w', 'b'

while not game_over:
    winner = 'White' if current_pawn == 'w' else 'Black'
    if current_pawn == 'w':
        result = white_checker(white_pawn_position[0][0], white_pawn_position[0][1])
        if not result:
            white_pawn_position[0][0] = white_pawn_position[0][0] - 1
            if white_pawn_position[0][0] == 0:
                game_over = True
                print(f"Game over! {winner} pawn is promoted to a queen at {columns[white_pawn_position[0][1]]}{size - white_pawn_position[0][0]}.")
        else:
            print(f"Game over! {winner} win, capture on {columns[white_pawn_position[0][1]]}{size - white_pawn_position[0][0]}.")
            game_over = True
    else:
        result = black_checker(black_pawn_position[0][0], black_pawn_position[0][1])
        if not result:
            black_pawn_position[0][0] = black_pawn_position[0][0] + 1
            if black_pawn_position[0][0] == 7:
                game_over = True
                print(f"Game over! {winner} pawn is promoted to a queen at {columns[black_pawn_position[0][1]]}{size - black_pawn_position[0][0]}.")
        else:
            print(f"Game over! {winner} win, capture on {columns[black_pawn_position[0][1]]}{size - black_pawn_position[0][0]}.")
            game_over = True
    current_pawn, second_pawn = second_pawn, current_pawn
