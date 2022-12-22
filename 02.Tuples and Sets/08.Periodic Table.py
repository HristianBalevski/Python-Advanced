count_of_elements = int(input())
periodic_table = set()

for _ in range(count_of_elements):
    chemical_elements = [el for el in input().split()]

    for element in chemical_elements:
        periodic_table.add(element)
print(*periodic_table, sep="\n")