def generate_pairs(m, n):
    return [(emme, enne) for emme in range(m, n + 1) for enne in range(emme, n + 1)]
