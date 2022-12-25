from collections import deque

data = deque(input().split())

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
all_colors = []

while data:
    first_string = data.popleft()
    last_string = data.pop() if data else ""

    color = first_string + last_string
    if color in main_colors or color in secondary_colors:
        all_colors.append(color)
        continue

    color = last_string + first_string
    if color in main_colors or color in secondary_colors:
        all_colors.append(color)
        continue

    first_string = first_string[:-1]
    last_string = last_string[:-1]

    if first_string:
        data.insert(len(data) // 2, first_string)

    if last_string:
        data.insert(len(data) // 2, last_string)

condition = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

final_result = []
is_collected = True

for col in all_colors:
    if col in main_colors:
        final_result.append(col)

    elif col in secondary_colors:
        for all_col in condition[col]:
            if all_col not in all_colors:
                is_collected = False
                break
        if is_collected:
            final_result.append(col)
print(final_result)
