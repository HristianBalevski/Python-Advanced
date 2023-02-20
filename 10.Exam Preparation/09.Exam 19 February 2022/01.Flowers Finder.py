from collections import deque

vowels = deque(input().split())
constants = input().split()

given_words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}
word_found = False

while True:
    if len(vowels) == 0 or len(constants) == 0:
        break

    vols = vowels.popleft()
    cons = constants.pop()

    for word in given_words.keys():
        given_words[word] = given_words[word].replace(vols, '')
        given_words[word] = given_words[word].replace(cons, '')

        if given_words[word] == '':
            print(f"Word found: {word}")
            word_found = True
            break
    if word_found:
        break

if not word_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if constants:
    print(f"Consonants left: {' '.join(constants)}")
