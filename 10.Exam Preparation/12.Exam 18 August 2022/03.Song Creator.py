def add_songs(*args):
    songs = {}
    output = []

    for info in args:
        title = info[0]
        text = info[1]
        if title not in songs:
            songs[title] = []
            songs[title].extend(text)

        elif title in songs and text:
            songs[title].extend(text)

    for key, value in songs.items():
        output.append(f'- {key}')
        output.extend(value)
    return "\n".join(output)
