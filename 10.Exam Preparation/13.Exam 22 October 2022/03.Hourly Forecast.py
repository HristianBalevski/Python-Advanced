def forecast(*args):
    my_dict = {}

    for info in args:
        my_dict[info[0]] = info[1]
    sorted_ditct = {k: v for k,v in sorted(my_dict.items(), key=lambda x: (x[1], x[0]))}
    sunny = ''
    cloudy = ''
    rainy = ''

    for key, value in sorted_ditct.items():
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy
