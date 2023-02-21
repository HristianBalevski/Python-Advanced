from collections import deque

elfs_energy = deque([int(num) for num in input().split()])
materials = [int(num) for num in input().split()]

total_energy = 0
toys = 0
iteration = 0

while True:
    if len(elfs_energy) == 0 or len(materials) == 0:
        break

    elf = elfs_energy.popleft()

    if elf < 5:
        continue

    box = materials.pop()
    iteration += 1

    needed_energy = box
    toys_to_do = 1
    added_energy = 1

    if iteration % 3 == 0:
        toys_to_do = 2
        needed_energy *= 2

    if iteration % 5 == 0:
        toys_to_do = 0
        added_energy = 0

    if elf >= needed_energy:
        toys += toys_to_do
        total_energy += needed_energy
        elfs_energy.append(elf - (needed_energy - added_energy))
    else:
        materials.append(box)
        elfs_energy.append(elf * 2)

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if elfs_energy:
    print(f'Elves left: {", ".join([str(e) for e in elfs_energy])}')
if materials:
    print(f'Boxes left: {", ".join([str(b) for b in materials])}')
