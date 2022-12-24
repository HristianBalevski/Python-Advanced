from collections import deque

data = input().split()
operators = {'*': lambda a, b: a * b,
             '/': lambda a, b: a / b,
             '+': lambda a, b: a + b,
             '-': lambda a, b: a - b
             }

nums = deque()

for symbol in data:
    if symbol not in operators:
        nums.append(int(symbol))
    else:
        if len(nums) > 2:
            result = int(operators[symbol](nums.popleft(), nums.popleft()))
            nums.appendleft(result)

            if len(nums) == 2:
                result = int(operators[symbol](nums.popleft(), nums.pop()))
                nums.appendleft((int(result)))
            continue
        left = nums.popleft()
        right = nums.pop()
        result = operators[symbol](left, right)
        nums.appendleft(abs(int(result)))
print(*nums)