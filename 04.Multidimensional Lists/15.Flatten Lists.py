data = input().split('|')
output = []

for index in range(len(data) - 1, -1, -1):
    elements = data[index].strip().split()
    output.extend(elements)
    
print(" ".join(output))
