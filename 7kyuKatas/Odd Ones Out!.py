def odd_ones_out(li):
    lis = li.copy()
    for i in li:
        if li.count(i)%2 != 0:
            lis.remove(i)
    return lis
