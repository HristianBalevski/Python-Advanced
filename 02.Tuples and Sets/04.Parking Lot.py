number_of_cars = int(input())
parking = set()

for _ in range(number_of_cars):
    direction, car_number = input().split(', ')
    
    if direction == 'IN':
        parking.add(car_number)

    elif direction == 'OUT':
        parking.remove(car_number)

if parking:
    for info in parking:
        print(info)
else:
    print('Parking Lot is Empty')