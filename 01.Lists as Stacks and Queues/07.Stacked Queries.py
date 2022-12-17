n = int(input())
stack = []

for _ in range(n):
    query = [num for num in input().split()]
    if query[0] == '1':
        stack.append(query[1])

    elif query[0] == '2' and stack:
        stack.pop()

    elif query[0] == '3' and stack:
        print(max(stack))

    elif query[0] == '4' and stack:
        print(min(stack))

while stack:
    if len(stack) > 1:
        print(stack.pop(), end=', ')
    else:
        print(stack.pop(), end='')