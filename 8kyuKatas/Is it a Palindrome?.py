def is_palindrome(s):
    if s.lower() == s[::-1].lower():
        return True
    return False
