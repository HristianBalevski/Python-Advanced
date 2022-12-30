def sorting_cheeses(**kwargs):
    result = ''
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))

    for tuple_ in sorted_cheeses:
        result += tuple_[0] + '\n'
        quantity = sorted(tuple_[1], reverse=True)
        result += '\n'.join(map(str, quantity))
        result += '\n'

    return result.strip()
