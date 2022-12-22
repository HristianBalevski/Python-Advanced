number_of_lines = int(input())

even_numbers = set()
odd_numbers = set()
sum_letter_counter = 0

for i in range(1, number_of_lines + 1):
    name = input()

    for letter in name:
        sum_letter_counter += ord(letter)
    result = int(sum_letter_counter / i)

    if result % 2 == 0:
        even_numbers.add(result)
    else:
        odd_numbers.add(result)
    sum_letter_counter = 0

if sum(even_numbers) == sum(odd_numbers):
    print(*odd_numbers.union(even_numbers), sep=", ")

elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=", ")
else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep=", ")