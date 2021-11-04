def number(bus_stops):
    return sum([pair[0] - pair[1] for pair in bus_stops])
