import csv
import json
import re

db_input_path = "/Users/mathias/Documents/programming_workspace/DataViz/input/db.json"
db_output_path = "/Users/mathias/Documents/programming_workspace/DataViz/output/db_cleaned.csv"

with open(db_input_path) as infile:
    db = json.loads(infile.read())

db_data = db["RealEstates"]
regex = re.compile(".*\|")

with open(db_output_path, "w") as outfile:
    f = csv.writer(outfile)
    f.writerow(["link", "address", "price", "additional_cost", "space"])
    for x in range(0,len(db_data)):
	    d = db_data[x]
	    address = d["address"].replace(" Die vollständige Adresse der Immobilie erhalten Sie vom Anbieter.","")
	    address = regex.sub("",address)
	    f.writerow([d["link"], address, d["price"], d["additional_cost"], d["space"]])
