from collections import deque

materials = [int(num) for num in input().split()]
magic_levels = deque([int(num) for num in input().split()])

presents = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}

while materials and magic_levels:

    product = materials.pop()
    power = magic_levels.popleft()
    result = product + power

    if result < 100:
        if result % 2 == 0:
            result = (product * 2) + (power * 3)
        else:
            result *= 2
    if result >= 500:
        result /= 2

    if 100 <= result <= 199:
        presents['Gemstone'] += 1

    elif 200 <= result <= 299:
        presents['Porcelain Sculpture'] += 1

    elif 300 <= result <= 399:
        presents['Gold'] += 1

    elif 400 <= result <= 499:
        presents['Diamond Jewellery'] += 1
if presents['Gemstone'] >= 1 and presents['Porcelain Sculpture'] >= 1 or presents['Gold'] >= 1 and presents['Diamond Jewellery'] >= 1:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join([str(num) for num in materials])}')
if magic_levels:
    print(f'Magic left: {", ".join([str(num) for num in magic_levels])}')

for present, quantity in sorted(presents.items()):
    if quantity >= 1:
        print(f'{present}: {quantity}')
