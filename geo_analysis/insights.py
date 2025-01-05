from .distance_calculation import calculate_distance

def generate_insights(data, region):
    locations = []
    for loc in data:
      if region.lower() in loc["region"].lower():
          locations.append(loc)
    if not locations:
        return f"No locations found in {region} region."

    total_locations = len(locations)
    farthest_distance = 0
    farthest_pair = None

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            dist = calculate_distance(locations[i]["coordinates"], locations[j]["coordinates"])
            if dist > farthest_distance:
                farthest_distance = dist
                farthest_pair = (locations[i], locations[j])

    result = f"Region: {region}\nTotal Locations: {total_locations}\n"
    if farthest_pair:
        result += (f"Farthest Locations: {farthest_pair[0]['name']} and {farthest_pair[1]['name']} "
                   f"(Distance: {farthest_distance} km)")
    return result