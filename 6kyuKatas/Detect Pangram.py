""" 
tests: "The quick, brown fox jumps over the lazy dog!"
"sphinx of black quartz, judge my vow"
"I'm the son of Apollo"

do all the letters of the alphabet appear
"""

import string

def is_pangram(s):
    s = s.replace(" ", "").lower() # case insensitive
    f = {letter: 0 for letter in string.ascii_lowercase}
    for letter in s:
        if letter in string.punctuation or letter in string.digits: continue
        if letter in string.ascii_lowercase:
            f[letter] = 1
    if 0 in f.values(): return False
    return True
