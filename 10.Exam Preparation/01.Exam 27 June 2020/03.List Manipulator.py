from collections import deque


def list_manipulator(lst, first_param, second_param, *numbers):

    my_list = deque(lst)

    if first_param == 'add' and second_param == 'beginning':
        for num in reversed(numbers):
            my_list.appendleft(num)

    if first_param == 'add' and second_param == 'end':
        for num in numbers:
            my_list.append(num)

    if first_param == 'remove' and second_param == 'beginning':
        copy_list = my_list.copy()
        if numbers:
            counter = 0
            for _ in copy_list:
                my_list.popleft()
                counter += 1
                if counter == numbers[0]:
                    break
        else:
            my_list.popleft()

    if first_param == 'remove' and second_param == 'end':
        copy_list = my_list.copy()
        if numbers:
            counter = 0
            for _ in copy_list:
                my_list.pop()
                counter += 1
                if counter == numbers[0]:
                    break
        else:
            my_list.pop()
    return [num for num in my_list]
