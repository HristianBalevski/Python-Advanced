from collections import deque

textiles = deque([int(num) for num in input().split()])
medicaments = [int(num) for num in input().split()]

healing_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0
}

while textiles and medicaments:

    first_item = textiles.popleft()
    last_item = medicaments.pop()
    result = first_item + last_item

    if result == 30:
        healing_items['Patch'] += 1

    elif result == 40:
        healing_items['Bandage'] += 1

    elif result == 100:
        healing_items['MedKit'] += 1

    elif result > 100:
        healing_items['MedKit'] += 1
        result -= 100

        medicaments[-1] += result
    else:
        medicaments.append(last_item + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

sorted_dict = dict(sorted(healing_items.items(), key=lambda x: (-x[1], x[0])))

for name, amount in sorted_dict.items():
    if amount > 0:
        print(f'{name} - {amount}')

if textiles:
    print(f'Textiles left: {", ".join(str(num) for num in textiles)}')

elif medicaments:
    print(f'Medicaments left: {", ".join(str(num) for num in reversed(medicaments))}')
