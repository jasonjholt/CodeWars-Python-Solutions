def duplicate_encode(word):
    word = word.lower()
    res = ""
    for char in word:
        if word.count(char) > 1:
            res += r")"
        else: res += r"("
    return res
