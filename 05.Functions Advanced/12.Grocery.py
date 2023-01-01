def grocery_store(**kwargs):
    result = {}
    output = []
    for product, quantity in kwargs.items():
        result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    for key, value in result:
        output.append(f"{key}: {value}")
    return '\n'.join(output)