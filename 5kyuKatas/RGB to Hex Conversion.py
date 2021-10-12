def convert(color):
    """ converts each value in the tuple
    
    strips 0x hex identifier and capitalises the letter"""
    if color > 255:
        color = 255
    elif color < 0:
        color = 0
    conv = hex(color)[2:]
    if len(conv) < 2:
        conv = '0' + conv
    return conv.upper()

def rgb(r,g,b):
    """ concatenating all conversions """
    s = ""
    for a in r,g,b:
        s += convert(a)
    return s
