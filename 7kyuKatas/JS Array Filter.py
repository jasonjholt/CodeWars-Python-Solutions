# helper function
def is_even(num):
    return True if num%2 == 0 else False

def get_even_numbers(arr):
    return list(filter(is_even, arr))
