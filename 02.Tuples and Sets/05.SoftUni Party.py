number_of_guests = int(input())
reservation = set()
party = set()

for _ in range(number_of_guests):
    reservation_code = input()
    reservation.add(reservation_code)

guest = input()

while guest != 'END':
    party.add(guest)
    guest = input()

missing_people = reservation.difference(party)
print(len(missing_people))

for person in sorted(missing_people):
    print(person)
