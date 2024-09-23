import json
f = open("AzureServices.json", "r+")

data = json.load(f)
services = data["Items"]

f.close()