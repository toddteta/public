import json

# Load the GeoJSON file
file_path = "/mnt/data/geojson-counties-fips.json"
with open(file_path, "r") as file:
    geojson_data = json.load(file)

# Mapping of state FIPS codes to state names
fips_to_state = {
    "01": "Alabama",
    "02": "Alaska",
    "04": "Arizona",
    "05": "Arkansas",
    "06": "California",
    "08": "Colorado",
    "09": "Connecticut",
    "10": "Delaware",
    "11": "District of Columbia",
    "12": "Florida",
    "13": "Georgia",
    "15": "Hawaii",
    "16": "Idaho",
    "17": "Illinois",
    "18": "Indiana",
    "19": "Iowa",
    "20": "Kansas",
    "21": "Kentucky",
    "22": "Louisiana",
    "23": "Maine",
    "24": "Maryland",
    "25": "Massachusetts",
    "26": "Michigan",
    "27": "Minnesota",
    "28": "Mississippi",
    "29": "Missouri",
    "30": "Montana",
    "31": "Nebraska",
    "32": "Nevada",
    "33": "New Hampshire",
    "34": "New Jersey",
    "35": "New Mexico",
    "36": "New York",
    "37": "North Carolina",
    "38": "North Dakota",
    "39": "Ohio",
    "40": "Oklahoma",
    "41": "Oregon",
    "42": "Pennsylvania",
    "44": "Rhode Island",
    "45": "South Carolina",
    "46": "South Dakota",
    "47": "Tennessee",
    "48": "Texas",
    "49": "Utah",
    "50": "Vermont",
    "51": "Virginia",
    "53": "Washington",
    "54": "West Virginia",
    "55": "Wisconsin",
    "56": "Wyoming",
}

# Add new attributes to each feature in the GeoJSON
for feature in geojson_data["features"]:
    properties = feature["properties"]
    state_name = fips_to_state.get(properties["STATE"], "Unknown")
    properties["COUNTY_FIPS"] = f"{properties['STATE']}{properties['COUNTY']}"
    properties["DISPLAY_NAME"] = f"{properties['NAME']}, {state_name}"

# Save the updated GeoJSON to a new file
updated_file_path = "/mnt/data/updated_geojson_counties.json"
with open(updated_file_path, "w") as updated_file:
    json.dump(geojson_data, updated_file)

updated_file_path
