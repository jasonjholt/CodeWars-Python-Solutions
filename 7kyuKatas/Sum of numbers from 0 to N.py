# Sum of numbers from 0 to N | Javatlacati

def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    else:
        s = sum(range(n+1))
        el = [str(x) for x in range(n+1)]
        fin = ""
        for num in el:
            if num != el[-1]:
                fin += num+"+"
            else:
                fin += num + " = "
        fin += str(s)
        return fin
