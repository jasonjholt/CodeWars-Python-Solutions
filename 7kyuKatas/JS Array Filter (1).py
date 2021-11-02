# doesn't use the filter function

def get_even_numbers(arr):
    return list(num for num in arr if num % 2 == 0)
