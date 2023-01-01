def even_odd_filter(**kwargs):
    my_dict = {}

    for key, value in kwargs.items():
        parity = 0 if key == 'even' else 1
        my_dict[key] = []
        for num in value:
            if num % 2 == parity:
                my_dict[key].append(num)

    return dict(sorted(my_dict.items(), key=lambda kvp: -len(kvp[1])))