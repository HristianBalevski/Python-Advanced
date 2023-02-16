from collections import deque


def stock_availability(*args):
    inventory = deque(args[0])
    second_param = args[1]
    third_param = args[2:]

    if second_param == 'delivery':
        for flavour in third_param:
            inventory.append(flavour)

    elif second_param == 'sell':
        if third_param:
            x = isinstance(third_param[0], int)
            if x:
                for _ in range(third_param[0]):
                    inventory.popleft()
            else:
                for product in third_param:
                    if product in inventory:
                        while product in inventory:
                            inventory.remove(product)
        else:
            inventory.popleft()
    return [row for row in inventory]
