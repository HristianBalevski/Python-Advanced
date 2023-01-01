def age_assignment(*args, **kwargs):
    result = {}
    output = []

    for name in args:
        if name[0] in kwargs.keys():
            key = name[0]
            result[name] = kwargs[key]
    result = dict(sorted(result.items(), key=lambda kvp: kvp[0]))

    for key, value in result.items():
        output.append(f"{key} is {value} years old.")
    return '\n'.join(output)