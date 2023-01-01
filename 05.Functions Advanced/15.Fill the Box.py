from collections import deque


def fill_the_box(height, length, width, *args):
    size = height * length * width
    numbers = deque()
    for element in args:
        if element == 'Finish':
            break
        numbers.appendleft(int(element))

    while len(numbers) > 0:
        if size == 0:
            break
        num = numbers.popleft()

        if num <= size:
            size -= num
        else:
            num = num - size
            numbers.append(num)
            size = 0
    if size > 0:
        return f"There is free space in the box. You could put {size} more cubes."
    else:
        return f"No more free space! You have {sum(numbers)} more cubes."