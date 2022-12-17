data = input()
possible_start = '{(['
pairs = ['{}', '[]', '()']
balanced = True
opening_brackets = []

for char in data:
    if char in possible_start:
        opening_brackets.append(char)
    elif not opening_brackets:
        balanced = False
        break
    else:
        last_open_bracket = opening_brackets.pop()
        if last_open_bracket + char not in pairs:
            balanced = False
            break
if balanced:
    print('YES')
else:
    print('NO')