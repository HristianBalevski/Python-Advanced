from pyfiglet import figlet_format
from random import choice


def ascii_art(text):
    fonts = ['3-d', '3x5', '5lineoblique', 'acrobatic', 'alligator', 'alligator2', 'alphabet', 'avatar', 'banner',
             'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'bell', 'big', 'bigchief',
             'block', 'bubble', 'bulbhead', 'calgphy2', 'colossal', 'coinstak', 'computer']

    output = figlet_format(text, font=choice(fonts))
    return output


def triangle(num):
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(f'{col}', end='')
        print()

    for row in range(num, -1, - 1):
        for col in range(1, row):
            print(f'{col}', end='')
        print()


def mathematical_operations(float_num, operator, int_num):
    float_num = float(float_num)
    int_num = int(int_num)

    operations = {
        '/': lambda float_num, int_num: float_num / int_num,
        '*': lambda  float_num, int_num: float_num * int_num,
        '-': lambda float_num, int_num: float_num - int_num,
        '+': lambda float_num, int_num: float_num + int_num,
        '^': lambda float_num, int_num: float_num ** int_num
    }
    result = operations[operator](float_num, int_num)
    return f'{result:.2f}'


fibonacci = []


def create_sequence(number):
    fibonacci.clear()
    counter = 0
    f0 = 0
    f1 = 1

    while counter < number:
        fibonacci.append(f0)
        result = f0 + f1

        f0 = f1
        f1 = result
        counter += 1
    return ' '.join([str(num) for num in fibonacci])


def locate_index(number):
    if number in fibonacci:
        index = fibonacci.index(number)
        return f'The number - {number} is at index {index}'
    else:
        return f'The number {number} is not in the sequence'
