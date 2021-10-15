def stray(arr):
    for a in arr:
        if arr.count(a) == 1:
            return a
