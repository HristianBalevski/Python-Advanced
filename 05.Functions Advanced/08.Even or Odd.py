def even_odd(*args):
    command = args[-1]
    parity = 0 if command == "even" else 1
    result = []

    for index in range(len(args) - 1):
        current_number = args[index]
        if current_number % 2 == parity:
            result.append(current_number)
    return result