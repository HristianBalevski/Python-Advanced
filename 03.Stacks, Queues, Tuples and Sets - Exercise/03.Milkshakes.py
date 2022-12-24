from collections import deque

chocolates = [int(num) for num in input().split(', ')]
cups_of_milk = deque([int(num) for num in input().split(', ')])

milkshakes = 0

while True:
    if len(chocolates) == 0 or len(cups_of_milk) == 0 or milkshakes == 5:
        break
    chocolate = chocolates[-1]
    milk = cups_of_milk[0]

    if chocolate <= 0 or milk <= 0:
        if chocolate <= 0:
            chocolates.pop()

        if milk <= 0:
            cups_of_milk.popleft()
        continue

    if chocolate == milk:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] = chocolate - 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f'Chocolate: {", ".join([str(num) for num in chocolates])}')
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f'Milk: {", ".join([str(num) for num in cups_of_milk])}')
else:
    print("Milk: empty")