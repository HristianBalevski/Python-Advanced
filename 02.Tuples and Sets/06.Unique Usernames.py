number_of_names = int(input())
unique_names = set()

for num in range(number_of_names):
    names = input()
    unique_names.add(names)
    
for name in unique_names:
    print(name)