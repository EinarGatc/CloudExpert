import json
f = open("AmazonServices.json", "r+")

services = json.load(f)

f.close()