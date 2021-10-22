""" for each character in string return "(" if it only appears once else return ")" """
# list comprehensions confuse me

def duplicate_encode(word):
    return "".join([r"(" if word.lower().count(char) == 1 else r")" for char in word.lower()])
