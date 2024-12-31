from geo_analysis.data_handling import get_locations
from geo_analysis.filtering import filter_by_region
from geo_analysis.distance_calculation import calculate_distance
from geo_analysis.insights import generate_insights
from geo_analysis.location_viewer import view_locations
from geo_analysis.location_searching import search_location




def main():
    data = get_locations()
    while True:
        print("\nWelcome to the Geographical Data Analysis System")
        print("1. View Location Data")
        print("2. Filter Locations by Region")
        print("3. Calculate Distance Between Locations")
        print("4. Generate Region Insights")
        print("5. Search Locations")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_locations(data)
        elif choice == "2":
            region = input("Enter the region to filter (North, South, Central, East, West): ")
            filtered = filter_by_region(data, region)
            if filtered:
                view_locations(filtered)
            else:
                print(f"No locations found in {region} region.")
        elif choice == "3":
            loc1_id = input("Enter the first location ID: ")
            loc2_id = input("Enter the second location ID: ")
            loc1 = search_location(data, loc1_id)
            loc2 = search_location(data, loc2_id)
            if loc1 and loc2:
                distance = calculate_distance(loc1["coordinates"], loc2["coordinates"])
                print(f"Distance between {loc1['name']} and {loc2['name']}: {distance} km")
            else:
                print("Invalid location ID(s).")
        elif choice == "4":
            region = input("Enter the region: ")
            print(generate_insights(data, region))
        elif choice == "5":
            query = input("Enter the location name or ID: ")
            result = search_location(data, query)
            if result:
                print(f"Found Location: ID: {result['id']}, Name: {result['name']}, Region: {result['region']}, Coordinates: {result['coordinates']}")
            else:
                print("Location not found.")
        elif choice == "6":
            print("Thank you for using the Geographical Data Analysis System.")
            break
        else:
            print("Invalid choice. Please try again.")


main()