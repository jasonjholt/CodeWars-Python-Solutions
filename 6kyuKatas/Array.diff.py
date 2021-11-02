def array_diff(a, b):
    if len(b) == 0: return a
    for ib in b:
        while ib in a:
            a.remove(ib)
    return a
