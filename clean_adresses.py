import csv
import json


db_input_path = "/Users/mathias/Documents/programming_workspace/DataViz/input/db.json"
db_output_path = "/Users/mathias/Documents/programming_workspace/DataViz/output/db_cleaned.csv"

with open(db_input_path) as infile:
    db = json.loads(infile.read())

db_data = db["RealEstates"]

with open(db_output_path, "w") as outfile:
    f = csv.writer(outfile)
    f.writerow(["link", "address", "price", "additional_cost", "space"])
    for x in range(0,len(db_data)):
	    d = db_data[x]
	    add = d["address"].replace(" Die vollständige Adresse der Immobilie erhalten Sie vom Anbieter.","")
	    f.writerow([d["link"], add, d["price"], d["additional_cost"], d["space"]])
