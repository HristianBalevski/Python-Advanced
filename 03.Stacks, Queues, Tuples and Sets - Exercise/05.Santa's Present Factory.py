from collections import deque

materials_for_crafting_toys = [int(num) for num in input().split()]
magic_values = deque([int(num) for num in input().split()])

crafted_toys = {}
material = 0

while True:
    if len(materials_for_crafting_toys) == 0 or len(magic_values) == 0:
        break

    box = materials_for_crafting_toys.pop()
    magic = magic_values.popleft()

    if box == 0:
        if magic != 0:
            magic_values.appendleft(magic)
        continue

    if magic == 0:
        if box != 0:
            materials_for_crafting_toys.append(box)
        continue

    if material > 0:
        total_magic_level = material * magic
        material = 0
        materials_for_crafting_toys.append(box)
    else:
        total_magic_level = box * magic

    if total_magic_level == 150:
        if 'Doll' not in crafted_toys:
            crafted_toys['Doll'] = 0
        crafted_toys['Doll'] += 1

    elif total_magic_level == 250:
        if 'Wooden train' not in crafted_toys:
            crafted_toys['Wooden train'] = 0
        crafted_toys['Wooden train'] += 1

    elif total_magic_level == 300:
        if 'Teddy bear' not in crafted_toys:
            crafted_toys['Teddy bear'] = 0
        crafted_toys['Teddy bear'] += 1

    elif total_magic_level == 400:
        if 'Bicycle' not in crafted_toys:
            crafted_toys['Bicycle'] = 0
        crafted_toys['Bicycle'] += 1
    else:
        if total_magic_level < 0:
            total_magic_level = box + magic
            material += total_magic_level

        elif total_magic_level > 0:
            materials_for_crafting_toys.append(box)
            materials_for_crafting_toys[-1] = box + 15

if 'Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys or 'Doll' in crafted_toys and 'Wooden train' in crafted_toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_for_crafting_toys:
    materials_for_crafting_toys = reversed(materials_for_crafting_toys)
    print(f"Materials left: {', '.join([str(num) for num in materials_for_crafting_toys])}")

if magic_values:
    print(f"Magic left: {', '.join([str(num) for num in magic_values])}")

sorted_toys = {key: value for key, value in sorted(crafted_toys.items())}
for item, quantity in sorted_toys.items():
    print(f'{item}: {quantity}')
