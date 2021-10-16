import numpy as np

def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    return (round(((number_of_sides * (circle_radius**2)) / 2) * (np.sin((2*np.pi)/number_of_sides)), 3))
