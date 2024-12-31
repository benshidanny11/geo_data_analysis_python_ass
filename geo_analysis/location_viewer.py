def view_locations(data):
    for loc in data:
        print(f"ID: {loc['id']}, Name: {loc['name']}, Region: {loc['region']}, Coordinates: {loc['coordinates']}")