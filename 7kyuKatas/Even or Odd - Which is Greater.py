def even_or_odd(s):
    a = [int(a) for a in str(s)]
    even_sum, odd_sum = 0,0
    for b in a:
        if b%2 == 0:
            even_sum += b
        else:
            odd_sum += b
    if even_sum > odd_sum:
        return "Even is greater than Odd"
    elif odd_sum > even_sum:
        return "Odd is greater than Even"
    else: return "Even and Odd are the same"
