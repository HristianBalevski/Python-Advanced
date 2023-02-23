from collections import deque

sizes_of_egs = deque([int(num) for num in input().split(", ")])
sizes_of_paper = [int(num) for num in input().split(", ")]

filled_boxes = 0

while True:
    if len(sizes_of_paper) == 0 or len(sizes_of_egs) == 0:
        break

    egg = sizes_of_egs.popleft()

    if egg <= 0:
        continue

    if egg == 13:
        sizes_of_paper[0], sizes_of_paper[-1] = sizes_of_paper[-1], sizes_of_paper[0]
        continue
    paper = sizes_of_paper.pop()

    if egg + paper <= 50:
        filled_boxes += 1
    else:
        continue

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if sizes_of_egs:
    print(f'Eggs left: {", ".join([str(x) for x in sizes_of_egs])}')
if sizes_of_paper:
    print(f'Pieces of paper left: {", ".join([str(x) for x in sizes_of_paper])}')
