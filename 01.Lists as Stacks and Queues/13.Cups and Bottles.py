from collections import deque

cups_capacity = deque([int(num) for num in input().split()])
filled_bottles = [int(num) for num in input().split()]

wasted_water = 0
needed_water = 0

while True:
    if len(cups_capacity) == 0 or len(filled_bottles) == 0:
        break

    current_cup = cups_capacity[0]
    current_bottle = filled_bottles[-1]

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_capacity.popleft()
        filled_bottles.pop()
    else:
        needed_water = current_cup - current_bottle
        filled_bottles.pop()

        while needed_water > 0:
            current_bottle = filled_bottles[-1]

            if needed_water - current_bottle > 0:
                needed_water = needed_water - current_bottle
                filled_bottles.pop()
            else:
                wasted_water += current_bottle - needed_water
                filled_bottles.pop()
                cups_capacity.popleft()
                break
                
if len(cups_capacity) == 0:
    print(f'Bottles: {" ".join(str(num) for num in filled_bottles)}')
    print(f"Wasted litters of water: {wasted_water}")

elif len(filled_bottles) == 0:
    print(f'Cups: {" ".join(str(num) for num in cups_capacity)}')
    print(f"Wasted litters of water: {wasted_water}")
