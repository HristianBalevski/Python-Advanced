characters = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for index, row in enumerate(file):
        if index % 2 == 0:
            text = " ".join(reversed(row.strip().split()))
            for char in characters:
                text = text.replace(char, '@')
            print(text)
