from math import sqrt
# "coordinates": (-2.0100805,30.0752425)}, "coordinates": (-2.6013, 29.7494)
def calculate_distance(coord1, coord2):
    return round(sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2), 2)