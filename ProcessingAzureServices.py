"""
Python script to extract certain features from Azure Virtual Machines data
"""
import json
f = open("AzureServices.json", "r+")
data = json.load(f)
f.close()
services = data["Items"]
print(services)
