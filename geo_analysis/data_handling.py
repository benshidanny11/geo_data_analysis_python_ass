locations = [{"id": "L001", "name": "Kigali", "region": "Central", "coordinates": (-2.0100805,30.0752425)},
             {"id": "L002", "name": "Butare", "region": "Southern", "coordinates": (-2.6013, 29.7494)},
             {"id": "L003", "name": "Musanze", "region": "Northern", "coordinates": (-1.5021, 29.6831)},
             {"id": "L004", "name": "Rubavu", "region": "Western", "coordinates": (-1.6872, 29.3737)},
             {"id": "L005", "name": "Nyamata", "region": "Eastern", "coordinates": (-2.0145, 30.2653)},
             {"id": "L006", "name": "Huye", "region": "Southern", "coordinates": (-2.9205, 29.7464)},
             {"id": "L007", "name": "Gisenyi", "region": "Western", "coordinates": (-1.6969, 29.2401)},
             {"id": "L008", "name": "Kayonza", "region": "Eastern", "coordinates": (-1.6597, 30.4953)},
             {"id": "L009", "name": "Ruhengeri", "region": "Northern", "coordinates": (1.4591516,29.6401661)},
             {"id": "L010", "name": "Gicumbi", "region": "Northern", "coordinates": (-1.6549, 29.8119)}]


def get_locations():
    return locations


def view_locations(data):
    for loc in data:
        print(f"ID: {loc['id']}, Name: {loc['name']}, Region: {loc['region']}, Coordinates: {loc['coordinates']}")
