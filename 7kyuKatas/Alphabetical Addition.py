def chars():
    """ generates a dictionary with the values of a:1, b:2, etc """
    char = {}
    keys = range(97, 123)
    values = range(1,27)
    for i in keys:
        char[chr(i)] = values[(i - 97)]
    return char

def charn():
    """ generates a dictionary with the values of 1:a, 2:b, etc """
    char = {}
    values = range(97, 123)
    keys = range(1,27) # scores
    for i in keys:
        char[i] = chr(96 + i)
    return char


def add_letters(*letters):
    char = chars()
    score = charn()
    sum = 0
    if len(letters) < 1: return "z"
    for letter in letters:
        sum += char[letter]
    while sum > 26:
        sum -= 26
    return score[sum]
