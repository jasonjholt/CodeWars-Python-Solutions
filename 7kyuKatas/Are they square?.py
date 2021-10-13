import numpy as np

def sqr(num):
    ten = int(np.sqrt(num))
    if ten**2 == num: return 1
    return 0

def is_square(arr):
    if len(arr) < 1:
        return None
    for num in arr:
        if sqr(num) == 0:
            return False
    return True
