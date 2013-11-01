import csv
stops = csv.DictReader(open("stops.txt"))

for stop in stops:
    latLon = stop["stop_lat"],stop["stop_lon"]
    street = stop["stop_street"]
    city = stop["stop_city"]
    print city, street, latLon
    
