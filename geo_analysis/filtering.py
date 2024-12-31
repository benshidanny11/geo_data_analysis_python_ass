def filter_by_region(data, region):
    return [location for location in data if region.lower() in location["region"].lower()]