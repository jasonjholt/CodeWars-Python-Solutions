from statistics import mean

def calculate_grade(grades):
    if mean(grades) >= 90 and mean(grades) <=100: return "A"
    elif mean(grades) >= 80 and mean(grades) <90: return "B"
    elif mean(grades) >= 70 and mean(grades) <80: return "C"
    elif mean(grades) >= 60 and mean(grades) <70: return "D"
    else: return "F"
