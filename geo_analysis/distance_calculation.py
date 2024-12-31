from math import sqrt

def calculate_distance(coord1, coord2):
    return round(sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2), 2)