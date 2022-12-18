numbers = (float(num) for num in input().split())
my_dict = {}

for number in numbers:
    if number not in my_dict:

        my_dict[number] = 0
    my_dict[number] += 1

for key, counter in my_dict.items():
    print(f"{key} - {counter} times")
