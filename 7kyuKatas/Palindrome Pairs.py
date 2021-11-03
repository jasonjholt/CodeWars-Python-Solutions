def palindrome_pairs(words):
    res = []
    for word in words:
        for word_s in words:
            if words.index(word) == words.index(word_s): continue
            st = str(word) + str(word_s)
            if st == st[::-1]: 
                res.append([words.index(word), words.index(word_s)])
    return res
