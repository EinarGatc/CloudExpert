import json
f = open("AmazonServices.json", "r+")

services = json.load(f)
print(services[0]["serviceCode"])
print(services[0]["product"]["attributes"].keys())
f.close()