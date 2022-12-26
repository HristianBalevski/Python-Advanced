from collections import deque

hive = deque([int(num) for num in input().split()])
floral_pollen = [int(num) for num in input().split()]
operators = deque(input().split())

possible_operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

total_honey = 0

while True:
    if len(hive) == 0 or len(floral_pollen) == 0:
        break

    bee = hive.popleft()
    nectar = floral_pollen.pop()

    if nectar < bee:
        hive.appendleft(bee)
        continue

    if nectar == 0:
        continue

    if nectar >= bee:
        action = operators.popleft()
        total_honey += abs(possible_operators[action](bee, nectar))

print(f"Total honey made: {total_honey}")
if hive:
    print(f'Bees left: {", ".join([str(num) for num in hive])}')

if floral_pollen:
    print(f'Nectar left: {", ".join([str(num) for num in floral_pollen])}')
