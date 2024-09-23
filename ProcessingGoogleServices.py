import json
f = open("GoogleServices.json", "r+")

data = json.load(f)
services = data["skus"]

f.close()