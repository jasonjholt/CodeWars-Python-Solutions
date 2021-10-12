def digital_root(n):
    while True: # won't stop until len(sum) == 1
        x = sum([int(a) for a in str(n)])
        if len(str(x)) > 1:
            n = x
        else:
            break
    return x
