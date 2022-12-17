from collections import deque

petrol_pumps = int(input())
pumps = deque()

for _ in range(petrol_pumps):
    pumps.append([int(num) for num in input().split()])

for index in range(petrol_pumps):
    bad_option = False
    tank = 0

    for petrol, distance in pumps:
        tank += petrol - distance
        if tank < 0:
            bad_option = True
            break
    if bad_option:
        pumps.append(pumps.popleft())
    else:
        print(index)
        break