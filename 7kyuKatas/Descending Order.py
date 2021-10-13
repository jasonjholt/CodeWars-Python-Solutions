def descending_order(num):
    s = []
    st = ""
    for digit in str(num):
        s.append(digit)
    for digit in sorted(s, reverse=True):
        st += str(digit)
    return int(st)
