number_of_iteration = int(input())
first_set = set()
second_set = set()
longest_intersection = []

for _ in range(number_of_iteration):
    data = input().split('-')
    first_start, first_end = data[0].split(',')
    second_start, second_end = data[1].split(',')

    first_start = int(first_start)
    first_end = int(first_end)
    second_start = int(second_start)
    second_end = int(second_end)

    for i in range(first_start, first_end + 1):
        first_set.add(i)

    for j in range(second_start, second_end + 1):
        second_set.add(j)

    result = first_set.intersection(second_set)

    if len(result) > len(longest_intersection):
        longest_intersection = result
    first_set = set()
    second_set = set()

print(f"Longest intersection is {[num for num in longest_intersection]} with length {len(longest_intersection)}")
