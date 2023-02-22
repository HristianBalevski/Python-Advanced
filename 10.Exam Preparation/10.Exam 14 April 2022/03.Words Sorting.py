def words_sorting(*args):
    my_dictionary = {}
    output = []
    total_sum = 0
    
    for word in args:
        sum_counter = 0
        for letter in word:
            sum_counter += ord(letter)
        my_dictionary[word] = sum_counter

    for value in my_dictionary.values():
        total_sum += value

    if total_sum % 2 == 0:
        sort_result = dict(sorted(my_dictionary.items(), key=lambda x: x[0]))
        for k, v in sort_result.items():
            output.append(f"{k} - {v}")
    else:
        sort_result = dict(sorted(my_dictionary.items(), key=lambda x: -x[1]))
        for k, v in sort_result.items():
            output.append(f"{k} - {v}")

    return '\n'.join(output)
