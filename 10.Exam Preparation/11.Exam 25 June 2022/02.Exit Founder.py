first, second = input().split(', ')
size = 6
matrix = [[el for el in input().split()] for _ in range(size)]
iteration = 0
tom_hit_wall = 0
jerry_hit_wall = 0

while True:
    row, col = eval(input())
    player = first if iteration % 2 == 0 else second
    iteration += 1

    if player == 'Tom' and tom_hit_wall % 2 != 0:
        tom_hit_wall = 0
        continue
    elif player == 'Jerry' and jerry_hit_wall % 2 != 0:
        jerry_hit_wall = 0
        continue

    if matrix[row][col] == 'E' or matrix[row][col] == 'T':
        opponent = ''
        if player == 'Tom':
            opponent = 'Jerry'
        else:
            opponent = 'Tom'
        if matrix[row][col] == 'E':
            print(f"{player} found the Exit and wins the game!")
        else:
            print(f"{player} is out of the game! The winner is {opponent}.")
        break

    if matrix[row][col] == 'W':
        if player == 'Tom':
            tom_hit_wall += 1
            print(f'{player} hits a wall and needs to rest.')
        else:
            jerry_hit_wall += 1
            print(f'{player} hits a wall and needs to rest.')
