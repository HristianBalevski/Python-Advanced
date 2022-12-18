number_of_students = int(input())
my_dict = {}

for _ in range(number_of_students):
    name, grades = input().split()
    grade = f'{float(grades):.2f}'

    if name not in my_dict:
        my_dict[name] = []
    my_dict[name].append(grade)

for n, g in my_dict.items():
    nums = [float(num) for num in g]
    average_grade = sum(nums) / len(nums)
    print(f'{n} -> {" ".join((str(num) for num in g))} (avg: {average_grade:.2f})')