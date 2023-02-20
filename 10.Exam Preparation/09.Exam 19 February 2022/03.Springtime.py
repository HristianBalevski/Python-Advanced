def start_spring(**kwargs):
    garden = {}
    output = []

    for key, value in kwargs.items():
        if value not in garden:
            garden[value] = []
        garden[value].append(key)

    sort_result = dict(sorted(garden.items(), key=lambda x: (-len(x[1]), x[0])))

    for k, v in sort_result.items():
        output.append(f'{k}:')
        for plant in sorted(v):
            output.append(f'-{plant}')
    return "\n".join(output)
