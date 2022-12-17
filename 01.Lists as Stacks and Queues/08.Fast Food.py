from collections import deque

quantity_of_the_food = int(input())
orders = deque([int(num) for num in input().split()])
print(max(orders))

while orders:
    if quantity_of_the_food >= orders[0]:
        quantity_of_the_food -= orders.popleft()
    else:
        break

if not orders:
    print("Orders complete")
else:
    print('Orders left: ', end='')
    while orders:
        print(f'{orders.popleft()}', end=' ')