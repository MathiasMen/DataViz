import csv
import time
from geopy.geocoders import Nominatim

db_input_path = "/Users/mathias/Documents/programming_workspace/DataViz/output/db_cleaned.csv"
db_output_path = "/Users/mathias/Documents/programming_workspace/DataViz/output/db_cleaned_with_coords.csv"

geo_locator = Nominatim(user_agent="DataViz")

with open(db_input_path) as infile:
    db_csv = csv.reader(infile, delimiter = ",")    
    next(db_csv) 
    with open(db_output_path,'w+') as outfile:
        db_csv_out = csv.writer(outfile)
        db_csv_out.writerow(["link", "address", "price", "additional_cost", "space","lat","lon"])
        counter = 0
        for row in db_csv:
            if counter < 100:
                coords = geo_locator.geocode(row[1])
                if coords != None:
                    lat = coords.latitude
                    lon = coords.longitude
                else:
                    lat = ""
                    lon = ""
                db_csv_out.writerow([row[0],row[1],row[2],row[3],row[4],lat,lon])
                counter += 1
