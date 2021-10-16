def persistence(n):
    if len(str(n))== 1: return 0
    persist = 0
    while len(str(n)) > 1:
        total = 1
        for digit in str(n):
            total *= int(digit)
        n = total
        persist += 1
    return persist
