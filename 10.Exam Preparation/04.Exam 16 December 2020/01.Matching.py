from collections import deque

males = [int(num) for num in input().split()]
females = deque([int(num) for num in input().split()])

matches = 0

while True:
    if len(females) == 0 or len(males) == 0:
        break

    man = males[-1]
    woman = females[0]

    if man <= 0:
        males.pop()
        continue
    if woman <= 0:
        females.popleft()
        continue

    if man % 25 == 0:
        males.pop()
        males.pop()
        continue
    if woman % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    if man == woman:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] = man - 2

print(f"Matches: {matches}")

if males:
    print(f'Males left: {", ".join(reversed([str(m) for m in males]))}')
else:
    print("Males left: none")

if females:
    print(f'Females left: {", ".join([str(f) for f in females])}')
else:
    print("Females left: none")
