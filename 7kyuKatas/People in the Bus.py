def number(bus_stops):
    people = 0
    for pair in bus_stops:
        people += (pair[0] - pair[1])
    return people
