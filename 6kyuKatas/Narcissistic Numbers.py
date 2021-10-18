def narcissistic( value ):
    sum = 0
    for digit in str(value):
        sum += int(digit) ** len(str(value))
    if sum == value: return True
    return False
