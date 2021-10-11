import re

def validate_pin(pin):
    if "\n" in pin:
        return False
    if re.match (r"[0-9]{4}$",pin):
        return True
    elif re.match (r"[0-9]{6}$",pin):
        return True
    return False
