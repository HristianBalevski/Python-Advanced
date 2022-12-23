first_set = {int(num) for num in input().split()}
second_set = {int(num) for num in input().split()}
number_of_commands = int(input())

for _ in range(number_of_commands):
    data = input().split()
    command = data[0]
    part_2 = data[1]
    numbers = [int(x) for x in data[2:]]

    if command == 'Add':
        if part_2 == 'First':
            first_set = first_set.union(numbers)
        else:
            second_set = second_set.union(numbers)

    elif command == 'Remove':
        if part_2 == 'First':
            first_set = first_set.difference(numbers)
        else:
            second_set = second_set.difference(numbers)
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
        
print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
