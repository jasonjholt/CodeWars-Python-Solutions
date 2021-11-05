def sum_str(a, b):
    if len(a) == 0:
        a = "0"
    if len(b) == 0:
        b = "0"
    return str(eval(a+"+"+b))
