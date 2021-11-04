def get_count(sentence):
    return len(["yes" for letter in sentence if letter in {'a','e','i','o','u'}])
