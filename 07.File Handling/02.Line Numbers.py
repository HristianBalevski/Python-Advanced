import re
from string import punctuation

pattern = r'[A-Za-z]'

with open('text.txt', 'r') as file, open('output.txt', 'w') as output:
    for index, row in enumerate(file):
        letter_counter = len(re.findall(pattern, row))
        punctuation_counter = len([el for el in row if el in punctuation])
        output.write(f'Line {index + 1}: {row.strip()} ({letter_counter})({punctuation_counter})\n')
