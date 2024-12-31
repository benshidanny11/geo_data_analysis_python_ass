def search_location(data, query):
    for loc in data:
        if loc['id'] == query or loc['name'].lower() == query.lower():
            return loc
    return None