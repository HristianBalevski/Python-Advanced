from collections import deque

seats = [x for x in input().split(", ")]
first_sequence = deque([int(num) for num in input().split(", ")])
second_sequence = deque([int(num) for num in input().split(", ")])

seat_matches = []
rotation = 0

while True:
    if len(seat_matches) == 3 or rotation == 10:
        break

    first_num = first_sequence.popleft()
    last_num = second_sequence.pop()
    
    symbol = chr(first_num + last_num)
    seat_1 = f'{first_num}{symbol}'
    seat_2 = f'{last_num}{symbol}'
    rotation += 1

    if seat_1 in seat_matches or seat_2 in seat_matches:
        continue

    if seat_1 in seats:
        seat_matches.append(seat_1)

    if seat_2 in seats:
        seat_matches.append(seat_2)

    if seat_1 not in seat_matches and seat_2 not in seat_matches:
        first_sequence.append(first_num)
        second_sequence.appendleft(last_num)

print(f"Seat matches: {', '.join([str(num) for num in seat_matches])}")
print(f"Rotations count: {rotation}")
