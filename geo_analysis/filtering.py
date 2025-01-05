def filter_by_region(data, region):
    locations=[]
    for loc in data:
        if region.lower() in loc['region'].lower() :
            locations.append(loc)
    return locations

def search_location(data, query):
    for loc in data:
        if loc['id'] == query or loc['name'].lower() == query.lower():
           return loc
