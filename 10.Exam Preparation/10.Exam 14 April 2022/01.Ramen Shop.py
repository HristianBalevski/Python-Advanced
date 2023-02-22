from collections import deque

bowls_of_ramen = [int(num) for num in input().split(', ')]
customers = deque([int(num) for num in input().split(', ')])

while True:
    if len(bowls_of_ramen) == 0 or len(customers) == 0:
        break

    ramen = bowls_of_ramen[-1]
    person = customers[0]

    if ramen == person:
        bowls_of_ramen.pop()
        customers.popleft()

    elif ramen > person:
        bowls_of_ramen[-1] = ramen - person
        customers.popleft()
    else:
        customers[0] = person - ramen
        bowls_of_ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(num) for num in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(num) for num in customers])}")
