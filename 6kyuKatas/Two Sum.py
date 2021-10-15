def two_sum(numbers, target):
    for num in numbers:
        for sub in numbers[numbers.index(num):]:
            if num + sub == target:
                if num == sub:
                    return (numbers.index(num), numbers.index(sub) + 1)
                else: return (numbers.index(num), numbers.index(sub))
