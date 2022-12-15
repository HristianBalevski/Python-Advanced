from collections import deque

customer = input()
qu = deque()

while customer != 'End':
    if customer == 'Paid':

        while qu:
            name = qu.popleft()
            print(name)
    else:
        qu.append(customer)
    customer = input()
print(f"{len(qu)} people remaining.")