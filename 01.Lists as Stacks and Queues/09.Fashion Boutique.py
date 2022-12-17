clothes_in_the_box = [int(num) for num in input().split()]
capacity_of_the_rack = int(input())
counter = 1
current_rack = 0

while clothes_in_the_box:
    item = clothes_in_the_box[-1]
    if current_rack + item <= capacity_of_the_rack:
        current_rack += item
        clothes_in_the_box.pop()
    else:
        counter += 1
        current_rack = 0
print(counter)