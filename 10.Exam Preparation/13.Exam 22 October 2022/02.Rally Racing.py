size = int(input())
tracked_car = input()

matrix = []
car_row = 0
car_col = 0
distance_covered = 0
found_t = 0
t_row = 0
t_col = 0

reach_the_final = False

moves = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1)
}

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'T':
            if found_t == 0:
                found_t += 1
            else:
                t_row = row
                t_col = col
    matrix.append(row_elements)

while True:
    command = input()
    if command == 'End':
        break

    my_row, my_col = moves[command](car_row, car_col)

    if matrix[my_row][my_col] == '.':
        distance_covered += 10

    elif matrix[my_row][my_col] == 'T':
        matrix[my_row][my_col] = '.'
        my_row = t_row
        my_col = t_col
        matrix[my_row][my_col] = '.'
        distance_covered += 30
    else:
        reach_the_final = True
        distance_covered += 10
        car_row = my_row
        car_col = my_col
        break
    car_row = my_row
    car_col = my_col

matrix[car_row][car_col] = 'C'

if reach_the_final:
    print(f"Racing car {tracked_car} finished the stage!")
else:
    print(f"Racing car {tracked_car} DNF.")
print(f"Distance covered {distance_covered} km.")

for r in matrix:
    print("".join(r))
