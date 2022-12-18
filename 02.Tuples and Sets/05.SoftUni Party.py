number_of_guests = int(input())
guests = set()

for _ in range(number_of_guests):
    reservation_code = input()
    guests.add(reservation_code)

invite = input()
while invite != 'END':

    if invite in guests:
        guests.remove(invite)
    invite = input()
print(len(guests))
print("\n".join(sorted(guests)))