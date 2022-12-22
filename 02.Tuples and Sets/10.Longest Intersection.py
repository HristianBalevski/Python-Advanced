number_of_lines = int(input())

first_intersection = []
second_intersection = []
current_intersection = []
longest_intersection = []
counter = 0

for _ in range(number_of_lines):
    data = input().split('-')

    for info in data:
        current_info = info.split(',')
        start = int(current_info[0])
        end = int(current_info[1])

        if counter == 0:
            for i in range(start, end + 1):
                first_intersection.append(i)
            counter += 1
        else:
            for i in range(start, end + 1):
                second_intersection.append(i)

    for num in first_intersection:
        if num in second_intersection:
            current_intersection.append(num)

    if len(longest_intersection) == 0:
        longest_intersection = current_intersection.copy()
    else:
        if len(longest_intersection) < len(current_intersection):
            longest_intersection = current_intersection.copy()
    first_intersection.clear()
    second_intersection.clear()
    current_intersection.clear()
    counter = 0
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")