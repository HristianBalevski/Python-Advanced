from collections import deque

milligrams_of_caffeinе = [int(num) for num in input().split(', ')]
energy_drinks = deque([int(num) for num in input().split(', ')])

stamats_caffeine = 0
MAXIMUM_CAFFEINE = 300

while True:
    if len(milligrams_of_caffeinе) == 0 or len(energy_drinks) == 0:
        break

    amount_of_caffeine = milligrams_of_caffeinе.pop()
    drink = energy_drinks.popleft()

    caffeine_in_the_drink = amount_of_caffeine * drink

    if caffeine_in_the_drink + stamats_caffeine <= MAXIMUM_CAFFEINE:
        stamats_caffeine += caffeine_in_the_drink
    else:
        energy_drinks.append(drink)
        if stamats_caffeine - 30 < 0:
            stamats_caffeine = 0
        else:
            stamats_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join([str(num) for num in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with { stamats_caffeine } mg caffeine.")
