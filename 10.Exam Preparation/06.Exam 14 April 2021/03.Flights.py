def flights(*args):

    flights_info = {}

    for index in range(0, len(args) - 1, 2):
        if args[index] == 'Finish':
            break
        else:
            city = args[index]
            passengers = args[index + 1]

            if city not in flights_info:
                flights_info[city] = 0
            flights_info[city] += passengers

    return flights_info
