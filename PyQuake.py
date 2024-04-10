import requests
import json
import sys

# The url you provided
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

# Command line options
simple = False

for arg in sys.argv:
    if arg == "/s":
        simple = True

# Get the contents of the URL
response = requests.get(url)

# Check for errors
if response.status_code != 200:
    print(f"Error: {response.status_code}")
else:
    # Parse the JSON data
    data = response.json()

    # Print the results in a more readable format
    print("Earthquakes Summary:\n")
    print("-" * 20)
    for feature in data['features']:
        properties = feature['properties']
        if not simple:
            print(f"Magnitude: {properties['mag']}")
            print(f"Location: {properties['place']}")
            print(f"URL: {properties['url']}\n")
        else:
            print(f"{properties['title']}\n")