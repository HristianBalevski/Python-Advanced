numbers = [int(num) for num in input().split(', ')]
copy_nums = sorted(numbers.copy())
searched_index = int(input())

clock_cycles = 0

for num in copy_nums:
    clock_cycles += num
    if num in numbers:
        index = numbers.index(num)
        if index == searched_index:
            break
        else:
            numbers[index] = 0
print(clock_cycles)
