from collections import deque

customers = deque([int(num) for num in input().split(', ')])
taxis = [int(num) for num in input().split(', ')]
total_time = 0

while customers and taxis:

    current_customer = customers[0]
    taxi = taxis.pop()

    if taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
    else:
        continue

if not customers:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(num) for num in customers])}')
