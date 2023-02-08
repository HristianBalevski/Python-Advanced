from collections import deque

bomb_effects = deque([int(num) for num in input().split(', ')])
bomb_casings = [int(num) for num in input().split(', ')]

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}
created_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

mission_completed = False

while bomb_effects and bomb_casings:

    first_bomb = bomb_effects[0]
    last_bomb = bomb_casings[-1]
    result = first_bomb + last_bomb

    if result in bombs:
        for number, name in bombs.items():
            if number == result:
                created_bombs[name] += 1
                bomb_effects.popleft()
                bomb_casings.pop()
                break
    else:
        bomb_casings[-1] -= 5

    if created_bombs['Datura Bombs'] >= 3 and created_bombs['Cherry Bombs'] >= 3 and created_bombs['Smoke Decoy Bombs'] >= 3:
        mission_completed = True
        print("Bene! You have successfully filled the bomb pouch!")
        break

if not mission_completed:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f'Bomb Effects: {", ".join([str(num) for num in bomb_effects])}')

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f'Bomb Casings: {", ".join([str(num) for num in bomb_casings])}')

for key, value in sorted(created_bombs.items()):
    print(f'{key}: {value}')
