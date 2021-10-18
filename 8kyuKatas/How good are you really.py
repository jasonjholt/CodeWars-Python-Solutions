from statistics import mean

def better_than_average(class_points, your_points):
    if mean(class_points) >= your_points:
        return False
    return True
