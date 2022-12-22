text = input()
my_dict = {}

for symbol in text:
    if symbol not in my_dict:
        my_dict[symbol] = 0
    my_dict[symbol] += 1

sorted_dict = {key: value for key, value in sorted(my_dict.items())}
for key, value in sorted_dict.items():
    print(f'{key}: {value} time/s')