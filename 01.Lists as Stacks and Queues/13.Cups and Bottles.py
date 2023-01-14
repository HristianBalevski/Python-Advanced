from collections import deque

cups_capacity = deque([int(num) for num in input().split()])
filled_bottles = [int(num) for num in input().split()]

wasted_water = 0

while True:
    if len(cups_capacity) == 0 or len(filled_bottles) == 0:
        break

    cup = cups_capacity.popleft()
    bottle = filled_bottles.pop()

    if bottle >= cup:
        wasted_water += bottle - cup
    else:
        while cup > 0:
            cup -= bottle
            bottle = filled_bottles.pop()

            if bottle >= cup:
                wasted_water += bottle - cup
                break

if filled_bottles:
    print(f'Bottles: {" ".join([str(num) for num in filled_bottles])}')

elif cups_capacity:
    print(f'Cups: {" ".join([str(num) for num in cups_capacity])}')

print(f'Wasted litters of water: {wasted_water}')
