from collections import deque

firework_effects = deque([int(num) for num in input().split(', ') if int(num) > 0])
explosive_power = [int(num) for num in input().split(', ') if int(num) > 0]

maria_dict = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}
firework_show = False

while True:
    if not firework_effects or not explosive_power:
        break
    effect = firework_effects.popleft()
    if effect == 0:
        continue
    power = explosive_power.pop()
    result = effect + power

    if result % 3 == 0 and result % 5 != 0:
        maria_dict['Palm Fireworks'] += 1

    elif result % 3 != 0 and result % 5 == 0:
        maria_dict['Willow Fireworks'] += 1

    elif result % 3 == 0 and result % 5 == 0:
        maria_dict['Crossette Fireworks'] += 1
    else:
        firework_effects.append(effect - 1)
        explosive_power.append(power)

    if maria_dict['Palm Fireworks'] >= 3 and maria_dict['Willow Fireworks'] >= 3 and maria_dict['Crossette Fireworks'] >= 3:
        firework_show = True
        break

if firework_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: {", ".join([str(num) for num in firework_effects])}')

if explosive_power:
    print(f'Explosive Power left: {", ".join([str(num) for num in explosive_power])}')

for key, value in maria_dict.items():
    print(f"{key}: {value}")
