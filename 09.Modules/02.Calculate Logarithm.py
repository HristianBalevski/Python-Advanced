from math import log


def calculate_logarithm(num, base):
    result = 0
    if base == 'natural':
        result = log(num)
    else:
        base = int(base)
        result = log(num, base)
    return f'{result:.2f}'


number = int(input())
data = input()
print(calculate_logarithm(number, data))
