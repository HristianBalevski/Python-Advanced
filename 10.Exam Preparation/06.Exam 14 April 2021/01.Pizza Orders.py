from collections import deque

pizza_orders = deque([int(num) for num in input().split(', ') if 0 < int(num) < 11])
employees = [int(num) for num in input().split(', ')]

total_pizzas = 0

while pizza_orders and employees:
    order = pizza_orders.popleft()
    current_employee = employees.pop()

    if order > current_employee:
        pizza_orders.appendleft(order - current_employee)
        total_pizzas += current_employee
        continue
    else:
        total_pizzas += order

if not pizza_orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(str(e) for e in employees)}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(str(o) for o in pizza_orders)}')
