from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)

    while numbers:
        number = numbers.popleft()

        kwargs['a'] += number
        if len(numbers) == 0:
            break

        number = numbers.popleft()
        kwargs['s'] -= number
        if len(numbers) == 0:
            break

        number = numbers.popleft()
        if number != 0:
            kwargs['d'] /= number

        if len(numbers) == 0:
            break

        number = numbers.popleft()
        kwargs['m'] *= number
        if len(numbers) == 0:
            break
    sorted_result = [f'{key}: {value:.1f}' for key, value in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))]
    return '\n'.join(sorted_result)