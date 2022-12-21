number_of_rows = int(input())

flatten_matrix = []

for iteration in range(number_of_rows):
    elements_for_column = [int(num) for num in input().split(', ')]
    flatten_matrix.extend(elements_for_column)

print(flatten_matrix)