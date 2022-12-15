from collections import deque

quantity = int(input())
data = input()
names = deque()

while data != 'Start':
    names.append(data)
    data = input()

command = input()
while command != 'End':
    if command.isdigit():
        litters = int(command)

        if quantity >= litters:
            quantity -= litters
            print(f"{names.popleft()} got water")
        else:
            print(f"{names.popleft()} must wait")
    else:
        command = command.split()
        added_litters = int(command[1])
        quantity += added_litters
    command = input()
print(f"{quantity} liters left")