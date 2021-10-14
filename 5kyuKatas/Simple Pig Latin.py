def pig_it(text):
    """ given text string, return string in pig latin """
    fin_list = []
    for word in text.split():
        if word.isalpha():
            fin_list.append(word[1:] + word[0] + "ay")
        else: fin_list.append(word)
    return ' '.join(fin_list)
