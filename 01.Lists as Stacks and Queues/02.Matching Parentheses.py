expression = input()
lst_indexes = []

for index in range(len(expression)):
    if expression[index] == '(':
        lst_indexes.append(index)

    elif expression[index] == ')':
        start_index = lst_indexes.pop()
        condition = expression[start_index:index + 1]
        print(condition)